#Coded By Sidra ELEzz
import zlib,base64
exec(zlib.decompress(base64.b64decode("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")))
