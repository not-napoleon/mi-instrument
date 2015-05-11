from mi.instrument.teledyne.workhorse.driver import NEWLINE

RSN_SAMPLE_RAW_DATA = (
"\x7f\x7f\x68\x08\x00\x06\x12\x00\x4d\x00\x8e\x00\xb0\x03\x42\x05\xd4\x06\x00\x00\x32\x28\xc8\x41\x00\x35\x04\x64\x01\x00\x80\x0c" +
"\xc0\x02\x01\x40\x11\x00\xd0\x07\x00\x01\x00\x00\x00\x00\x00\x00\x7d\x3d\xeb\x0f\x10\x0d\x01\x05\x32\x00\xc6\x00\x82\x00\x00\x06" +
"\xff\x23\xe5\x09\x00\x00\xff\x00\x0c\x48\x00\x00\x14\x80\x00\x05\x00\x0d\x03\x0f\x15\x21\x02\x2e\x00\x00\x00\xf3\x05\x00\x00\x65" +
"\x14\xcf\xed\x2f\xee\x23\x00\x02\x08" +
"\x00\x00\x00\x00\x00\x00\x74\xa9\x58\x4f\x4f\x00\x00\x00\x00\x00\x00\x00\x04\x90\x51\xf2\xff\xff\x00\x00\x00\x00\x00\x14\x0d\x03" +
"\x0f\x15\x21\x02\x2e\x00\x01\x13\x00\xf4\xff\xb3\x00\x4d\x00\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00" +
"\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00" +
"\x80\x00\x80\x00\x80\x00\x80\x00\x80" +
"\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80" +
"\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80" +
"\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80" +
"\x00\x80\x00\x80\x00\x80\x00\x80\x00" +
"\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00" +
"\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00" +
"\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00" +
"\x80\x00\x80\x00\x80\x00\x80\x00\x80" +
"\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80" +
"\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80" +
"\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80" +
"\x00\x80\x00\x80\x00\x80\x00\x80\x00" +
"\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00" +
"\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00" +
"\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00" +
"\x80\x00\x80\x00\x80\x00\x80\x00\x80" +
"\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80" +
"\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80" +
"\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80" +
"\x00\x80\x00\x80\x00\x80\x00\x80\x00" +
"\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00" +
"\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00" +
"\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00" +
"\x80\x00\x80\x00\x80\x00\x80\x00\x80" +
"\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80" +
"\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80" +
"\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80" +
"\x00\x80\x00\x80\x00\x80\x00\x80\x00" +
"\x02\x4d\x59\x57\x5d\x0f\x0d\x15\x0a\x07\x04\x08\x09\x07\x04\x10\x04\x07\x08\x0b\x09\x05\x09\x0b\x06\x07\x05\x0b\x09\x07\x0b\x05" +
"\x06\x05\x08\x07\x09\x09\x0d\x03\x06\x06\x03\x08\x0a\x0a\x0b\x07\x07\x05\x0a\x06\x09\x04\x04\x02\x06\x06\x07\x05\x06\x05\x02\x03" +
"\x0a\x04\x04\x0c\x07\x07\x07\x0d\x0c\x07\x05\x02\x0a\x0b\x09\x04\x07\x06\x02\x06\x0b\x0a\x0e\x06\x0a\x03\x07\x02\x07\x04\x02\x06" +
"\x09\x04\x0a\x08\x04\x04\x04\x06\x0b" +
"\x05\x03\x0b\x04\x02\x06\x0a\x06\x04\x05\x02\x07\x05\x0a\x0c\x05\x07\x07\x07\x0e\x05\x06\x0d\x06\x07\x09\x04\x02\x04\x08\x07\x09" +
"\x06\x09\x06\x0b\x07\x05\x07\x11\x02\x07\x07\x03\x04\x04\x08\x0a\x03\x04\x07\x09\x09\x08\x06\x03\x02\x07\x09\x07\x04\x07\x07\x06" +
"\x04\x09\x04\x06\x03\x07\x06\x0a\x04\x04\x03\x0d\x06\x0d\x0e\x09\x05\x06\x07\x04\x03\x04\x04\x08\x02\x09\x04\x0d\x04\x04\x09\x03" +
"\x02\x07\x07\x0a\x03\x04\x04\x01\x06" +
"\x09\x04\x0b\x0a\x0a\x06\x09\x07\x09\x07\x06\x05\x08\x09\x0c\x02\x0a\x03\x02\x07\x04\x08\x07\x05\x06\x09\x09\x06\x06\x06\x0a\x04" +
"\x06\x05\x0c\x06\x02\x05\x0c\x04\x08\x04\x07\x03\x09\x09\x08\x06\x06\x04\x06\x05\x02\x04\x0b\x04\x0b\x0b\x0e\x03\x05\x09\x0c\x05" +
"\x03\x02\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" +
"\x00\x00\x00\x00\x00\x00\x00\x00\x00" +
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" +
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" +
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x61\x5d\x71\x63\x2f\x2f\x38\x33" +
"\x29\x2a\x30\x2e\x28\x2a\x30\x2e\x28" +
"\x29\x30\x2e\x28\x29\x2f\x2e\x29\x29\x2f\x2e\x28\x29\x2f\x2e\x28\x2a\x2f\x2e\x28\x2a\x2f\x2e\x28\x29\x2e\x2d\x28\x29\x30\x2e\x28" +
"\x29\x30\x2e\x28\x2a\x2f\x2e\x28\x2a\x30\x2e\x28\x2a\x30\x2e\x28\x2a\x2f\x2e\x28\x29\x2f\x2e\x28\x29\x2f\x2e\x27\x29\x2f\x2e\x28" +
"\x29\x2f\x2e\x28\x2a\x2f\x2d\x28\x29\x2f\x2e\x28\x2a\x2f\x2d\x29\x2a\x2f\x2e\x28\x2a\x30\x2e\x28\x2a\x2f\x2e\x28\x2a\x2f\x2e\x28" +
"\x29\x2f\x2e\x27\x29\x30\x2e\x28\x2a" +
"\x2f\x2f\x28\x2a\x2f\x2e\x28\x29\x30\x2e\x28\x29\x30\x2e\x29\x29\x2f\x2e\x27\x29\x2f\x2d\x28\x29\x30\x2e\x28\x29\x2f\x2e\x28\x29" +
"\x30\x2d\x28\x29\x2e\x2d\x28\x29\x2f\x2e\x28\x2a\x30\x2f\x28\x29\x30\x2d\x28\x29\x2f\x2d\x28\x29\x2f\x2e\x28\x2a\x2f\x2e\x28\x29" +
"\x2f\x2d\x28\x29\x2f\x2d\x28\x29\x2f\x2e\x28\x29\x30\x2e\x28\x29\x2f\x2e\x28\x29\x2e\x2e\x28\x29\x2f\x2e\x29\x29\x30\x2e\x28\x29" +
"\x30\x2e\x28\x2a\x30\x2e\x28\x29\x2f" +
"\x2d\x28\x29\x2f\x2d\x28\x2a\x2f\x2e\x28\x29\x2f\x2d\x28\x29\x2f\x2e\x28\x29\x2f\x2e\x28\x2a\x2f\x2e\x28\x29\x2e\x2d\x29\x29\x2f" +
"\x2e\x28\x29\x2e\x2d\x28\x29\x2f\x2e\x28\x2a\x2f\x2e\x28\x29\x2f\x2e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" +
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" +
"\x00\x00\x00\x00\x00\x00\x00\x00\x00" +
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" +
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" +
"\x00\x00\x00\x00\x00\x04\x64\x64\x64\x64\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" +
"\x00\x00\x00\x00\x00\x00\x00\x00\x00" +
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" +
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" +
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" +
"\x00\x00\x00\x00\x00\x00\x00\x00\x00" +
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" +
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" +
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" +
"\x00\x00\x00\x00\x00\x00\x00\x00\x00" +
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" +
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" +
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" +
"\x00\x00\x00\x00\x00\x00\x00\x00\x00" +
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" +
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7d\xf2\x2f\x20")

EF_CHAR = "\xef"

RSN_CALIBRATION_RAW_DATA = [
"ACTIVE FLUXGATE CALIBRATION MATRICES in NVRAM" + NEWLINE,
"               Calibration date and time: 9/14/2012  09:25:32" + NEWLINE,
"                             S inverse" + NEWLINE,
"          " + EF_CHAR + "                                                  " + EF_CHAR + NEWLINE,
"     Bx   " + EF_CHAR + "   3.9218e-01  3.9660e-01 -3.1681e-02  6.4332e-03 " + EF_CHAR + NEWLINE,
"     By   " + EF_CHAR + "  -2.4320e-02 -1.0376e-02 -2.2428e-03 -6.0628e-01 " + EF_CHAR + NEWLINE,
"     Bz   " + EF_CHAR + "   2.2453e-01 -2.1972e-01 -2.7990e-01 -2.4339e-03 " + EF_CHAR + NEWLINE,
"     Err  " + EF_CHAR + "   4.6514e-01 -4.0455e-01  6.9083e-01 -1.4291e-02 " + EF_CHAR + NEWLINE,
"          " + EF_CHAR + "   )                                               " + EF_CHAR + NEWLINE,
"                             Coil Offset" + NEWLINE,
"                         " + EF_CHAR + "                " + EF_CHAR + NEWLINE,
"                         " + EF_CHAR + "   3.4233e+04   " + EF_CHAR + NEWLINE,
"                         " + EF_CHAR + "   3.4449e+04   " + EF_CHAR + NEWLINE,
"                         " + EF_CHAR + "   3.4389e+04   " + EF_CHAR + NEWLINE,
"                         " + EF_CHAR + "   3.4698e+04   " + EF_CHAR + NEWLINE,
"                         " + EF_CHAR + "                " + EF_CHAR + NEWLINE,
"                             Electrical Null" + NEWLINE,
"                              " + EF_CHAR + "       " + EF_CHAR + NEWLINE,
"                              " + EF_CHAR + " 34285 " + EF_CHAR + NEWLINE,
"                              " + EF_CHAR + "       " + EF_CHAR + NEWLINE,
"                    TILT CALIBRATION MATRICES in NVRAM" + NEWLINE,
"                Calibration date and time: 9/14/2012  09:14:45" + NEWLINE,
"              Average Temperature During Calibration was   24.4 " + EF_CHAR + "C" + NEWLINE,
NEWLINE,
"                   Up                              Down" + NEWLINE,
NEWLINE,
"        " + EF_CHAR + "                           " + EF_CHAR + "     " + EF_CHAR + "                           " + EF_CHAR + NEWLINE,
" Roll   " + EF_CHAR + "   7.4612e-07  -3.1727e-05 " + EF_CHAR + "     " + EF_CHAR + "  -3.0054e-07   3.2190e-05 " + EF_CHAR + NEWLINE,
" Pitch  " + EF_CHAR + "  -3.1639e-05  -6.3505e-07 " + EF_CHAR + "     " + EF_CHAR + "  -3.1965e-05  -1.4881e-07 " + EF_CHAR + NEWLINE,
"        " + EF_CHAR + "                           " + EF_CHAR + "     " + EF_CHAR + "                           " + EF_CHAR + NEWLINE,
NEWLINE,
"        " + EF_CHAR + "                           " + EF_CHAR + "     " + EF_CHAR + "                           " + EF_CHAR + NEWLINE,
" Offset " + EF_CHAR + "   3.2808e+04   3.2568e+04 " + EF_CHAR + "     " + EF_CHAR + "   3.2279e+04   3.3047e+04 " + EF_CHAR + NEWLINE,
"        " + EF_CHAR + "                           " + EF_CHAR + "     " + EF_CHAR + "                           " + EF_CHAR + NEWLINE,
NEWLINE,
"                             " + EF_CHAR + "       " + EF_CHAR + NEWLINE,
"                      Null   " + EF_CHAR + " 33500 " + EF_CHAR + NEWLINE,
"                             " + EF_CHAR + "       " + EF_CHAR + NEWLINE,
NEWLINE,
NEWLINE,
NEWLINE,
NEWLINE,
NEWLINE,
">"]

RSN_CALIBRATION_RAW_DATA = ''.join(RSN_CALIBRATION_RAW_DATA)

RSN_PS0_RAW_DATA = (
"Instrument S/N:  18444" + NEWLINE +
"       Frequency:  76800 HZ" + NEWLINE +
"   Configuration:  4 BEAM, JANUS" + NEWLINE +
"     Match Layer:  10" + NEWLINE +
"      Beam Angle:  20 DEGREES" + NEWLINE +
"    Beam Pattern:  CONVEX" + NEWLINE +
"     Orientation:  UP" + NEWLINE +
"       Sensor(s):  HEADING  TILT 1  TILT 2  DEPTH  TEMPERATURE  PRESSURE" + NEWLINE +
"Pressure Sens Coefficients:" + NEWLINE +
"              c3 = -1.927850E-11" + NEWLINE +
"              c2 = +1.281892E-06" + NEWLINE +
"              c1 = +1.375793E+00" + NEWLINE +
"          Offset = +1.338634E+01" + NEWLINE +
NEWLINE +
"Temp Sens Offset:  -0.01 degrees C" + NEWLINE +
NEWLINE +
"    CPU Firmware:  50.40 [0]" + NEWLINE +
"   Boot Code Ver:  Required:  1.16   Actual:  1.16" + NEWLINE +
"    DEMOD #1 Ver:  ad48, Type:  1f" + NEWLINE +
"    DEMOD #2 Ver:  ad48, Type:  1f" + NEWLINE +
"    PWRTIMG  Ver:  85d3, Type:   7" + NEWLINE +
NEWLINE +
"Board Serial Number Data:" + NEWLINE +
"   72  00 00 06 FE BC D8  09 HPA727-3009-00B " + NEWLINE +
"   81  00 00 06 F5 CD 9E  09 REC727-1004-06A" + NEWLINE +
"   A5  00 00 06 FF 1C 79  09 HPI727-3007-00A" + NEWLINE +
"   82  00 00 06 FF 23 E5  09 CPU727-2011-00E" + NEWLINE +
"   07  00 00 06 F6 05 15  09 TUN727-1005-06A" + NEWLINE +
"   DB  00 00 06 F5 CB 5D  09 DSP727-2001-06H" + NEWLINE +
">")

PT2_RAW_DATA = (
"Ambient  Temperature =    20.32 Degrees C" + NEWLINE +
"  Attitude Temperature =    24.65 Degrees C" + NEWLINE +
"  Internal Moisture    = 8F0Ah" + NEWLINE +
">")

PT4_RAW_DATA = (
"IXMT    =      2.0 Amps rms  [Data=b0h]" + NEWLINE +
"VXMT    =     60.1 Volts rms [Data=9eh]" + NEWLINE +
"   Z    =     29.8 Ohms"  + NEWLINE +
"Transmit Test Results = $0 ... PASS"  + NEWLINE +
">")