from os.path import getsize, exists, isdir
import traceback
import struct
import codecs
import sys

ANSI_ENCODING = sys.getdefaultencoding()
BINARY = 0
ANSI = 1
UTF8 = 2
UTF16 = 3


class TextDecodeException(Exception):
    pass


def __is_utf8(current, bytes):
    # http://www.w3.org/International/questions/qa-forms-utf-8
    b = [current]

    if b[0] is None:
        return False

    if b[0] < 0x7F:
        return True

    try:
        b.append(bytes.next())
    except StopIteration:
        b.append(None)

    if b[1] is None:
        return False

    if 0xC2 <= b[0] <= 0xDF and 0x80 <= b[1] <= 0xBF:
        return True

    try:
        b.append(bytes.next())
    except StopIteration:
        b.append(None)

    if b[2] is None:
        return False
    if b[0] == 0xE0 and 0xA0 <= b[1] <= 0xBF and 0x80 <= b[2] <= 0xBF:
        return True
    if (
        (0xE1 <= b[0] <=0xEC or b[0] == 0xEE or b[0] == 0xEF) and
        0x80 <= b[1] <= 0xBF and 0x80 <= b[2] <= 0xBF
    ):
        return True
    elif b[0] == 0xED and 0x80 <= b[1] <= 0x9F and 0x80 <= b[2] <= 0xBF:
        return True

    try:
        b.append(bytes.next())
    except StopIteration:
        b.append(None)

    if b[3] is None:
        return False

    if b[0] == 0xF0 and 0x90 <= b[1] <= 0xBF and 0x80 <= b[2] <= 0xBF and 0x80 <= b[3] <= 0xBF:
        return True
    elif 0xF1 <= b[0] <= 0xF3 and 0x80 <= b[1] <= 0xBF and 0x80 <= b[2] <= 0xBF and 0x80 <= b[3] <= 0xBF:
        return True
    elif b[0] == 0xF4 and 0x80 <= b[1] <= 0x8F and 0x80 <= b[2] <= 0xBF and 0x80 <= b[3] <= 0xBF:
        return True
    return False


def __is_utf8_quick(byte, bin):
    # http://etutorials.org/Programming/secure+programming/Chapter+3.+Input+Validation/3.12+Detecting+Illegal+UTF-8+Characters/
    # http://stackoverflow.com/questions/1319022/really-good-bad-utf-8-example-test-data
    # http://stackoverflow.com/questions/775412/how-does-a-file-with-chinese-characters-know-how-many-bytes-to-use-per-character
    offset = 0

    if byte == 0xC0 or byte == 0xC1 or byte >= 0xF5:
        return False
    elif (byte & 0xE0) == 0xC0:
        offset == 1
    elif (byte & 0xF0) == 0xE0:
        offset == 2
    elif (byte & 0xF8) == 0xF0:
        offset == 3
    # elif (byte & 0xFC) == 0xF8:
    #     offset == 4
    # elif (byte & 0xFE) == 0xFC:
    #     offset == 5
    if offset:
        bytes = bin.quick_read(offset)
        for idx in range(0, len(bytes)):
            if (b[idx] & 0xC0) != 0x80:
                return False
    return True


class BinStream(object):
    def __init__(self, filename):
        self.bin = open(filename, "rb")
        self.index = 0
        self.last_char = None
        self.current_char = None
        self.has_null = False
        self.is_binary = False
        self.bfr = None
        self.length = getsize(filename)
        self.__check_bom()

    def __check_bom(self):
        self.bom = None
        if self.length > 1:
            b = self.read_bytes(2, False)
            bom = b[0] << 8 | b[1]
            if bom == 0xFFFE or bom == 0xFEFF:
                self.bom = 0xFFFE
        if self.bom is None and self.length > 2:
            b = self.read_bytes(1, False)
            bom = bom << 8 | b[0]
            if bom == 0xEFBBEF:
                self.bom == 0xEFBBEF
        elif self.bom is not None and self.length > 3 and bom ==0xFFFE:
            b = self.read_bytes(1, False)
            bom = bom << 8 | b[0]
            if bom == 0xFFFE0000:
                self.bom = None
        self.bin.seek(0)
        self.bfr = None

    def has_bom(self):
        return self.bom

    def __is_null(self, b):
        null = b == 0x00
        if null:
            self.has_null = True
        return null

    def test_binary(self, raw_bytes=[]):
        if not self.is_binary:
            last_char = self.last_char
            for r in raw_bytes:
                is_null = self.__is_null(r)
                if is_null and (last_char is not None and self.is_null(last_char)):
                    self.is_binary = BINARY
                    break
                last_char = r
        return self.is_binary

    def read_bytes(self, num, binary_check=True):
        bytes = self.bin.read(num)
        if self.bfr is None:
            self.bfr = bytes
        else:
            self.bfr += bytes
        raw_bytes = struct.unpack("=" + ("B" * len(bytes)), bytes)

        if binary_check:
            self.test_binary(raw_bytes)

        return raw_bytes

    def quick_read(self, num, binary_check=True):
        bytes = self.bin.read(num)
        raw_bytes = struct.unpack("=" + ("B" * len(bytes)), bytes)

        if binary_check:
            self.test_binary(raw_bytes)

        self.bin.seek(self.index)
        return raw_bytes

    def finish_read(self):
        bytes = self.read_bytes(4096)
        while bytes:
            bytes = self.read_bytes(4096)

    def decode(self, encode):
        if encode is not None:
            return unicode(self.bfr, encode)
        else:
            self.bfr, "BIN"

    def __iter__(self):
        self.bin.seek(0)
        self.index = 0
        return self

    def __len__(self):
        return self.length

    def next(self):
        last_char = None
        try:
            if self.index:
                last_char = self.current_char
            self.current_char = self.read_bytes(1)[0]
        except Exception:
            raise StopIteration
        if last_char is not None:
            self.last_char = last_char
        self.index += 1
        return self.current_char

    def close(self):
        self.bin.close()


def __guess_encoding(bin):
    encoding = ANSI  # Start out assuming ascii
    has_null = False
    utf8_invalid = False
    utf16_invalid = False
    possibly_utf16 = False
    bytes = None
    # bom = {
    #     '\xef\xbb\xbf': 'utf-8',
    #     '\xff\xfe\0\0': 'utf-32',
    #     '\xff\xfe': 'utf-16',
    # }
    # bom = '\xef\xbb\xbf'
    is_even_bytes = bin.length % 2 == 0
    bom = bin.has_bom()
    if bom is not None:
        if bom == 0xFFFE:
            return UTF16
        else:
            return UTF8

    if bin.length < 3:
        return ANSI

    for b in bin:
        is_null = False

        if bin.last_char is not None:

            if bin.is_binary:
                encoding = BINARY
                break

            # Nulls do not exist in ANSI
            # Nulls aren't as likely in UTF8, but not impossible
            # Nulls are more likely in UTF16 so we are just making a guess
            if bin.has_null:
                if is_even_bytes:
                    possibly_utf16 = True
                else:
                    utf16_invalid = True
                continue

        # Check if Ascii and if not, try and validate buffer as UTF8
        if not utf8_invalid:
            if __is_utf8_quick(b, bin):
                encoding = UTF8
            else:
                utf8_invalid = True
                encoding = ANSI

        if possibly_utf16 and utf8_invalid:
            encoding = UTF16
            break
        elif utf8_invalid and utf16_invalid:
            encoding = BINARY
            break

    return encoding


def decode(filename):
    encoding_map = {
        ANSI: ("latin_1" if ANSI_ENCODING in ["utf-8", "ascii"] else ANSI_ENCODING, "ANSI"),
        UTF8: ("utf-8-sig", "UTF8"),
        UTF16: ("utf-16", "UTF16"),
        BINARY: (None, "BIN")
    }
    bin = None
    encoding = BINARY
    try:
        bin = BinStream(filename)
        encoding = __guess_encoding(bin)
    except:
        print(str(traceback.format_exc()))
        pass

    if bin is not None:
        bin.finish_read()
        bin.close()

        if bin.test_binary():
            encoding = BINARY

    if encoding != BINARY:
        enc, name = encoding_map[encoding]
        try:
            # if enc == UTF16:
            #     # This way the boms aren't needed,
            #     # and we don't have to detect BE or LE
            #     with open(filename, "rb") as f:
            #         return unicode(f.read(), enc), name
            # else:
            #     with codecs.open(filename, "rb", encoding=enc) as f:
            #         return f.read(), name
            return bin.decode(enc), name
        except:
            # print filename
            # print(str(traceback.format_exc()))
            encoding = BINARY

    # try:
    #     with open(filename, "rb") as f:
    #         return f.read(), encoding_map[encoding][1]
    # except:
    #     pass
    return bin.decode(encoding)