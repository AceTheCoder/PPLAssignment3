# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\63")
        buf.write("\u0186\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26")
        buf.write("\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'")
        buf.write("\3\'\3(\3(\3)\3)\3)\3)\7)\u0106\n)\f)\16)\u0109\13)\3")
        buf.write(")\3)\3*\3*\3*\3*\7*\u0111\n*\f*\16*\u0114\13*\3*\3*\3")
        buf.write("*\3*\3*\3+\3+\5+\u011d\n+\3,\6,\u0120\n,\r,\16,\u0121")
        buf.write("\3-\3-\5-\u0126\n-\3-\3-\3-\3-\3-\5-\u012d\n-\3.\3.\3")
        buf.write(".\3/\3/\5/\u0134\n/\3/\5/\u0137\n/\5/\u0139\n/\3\60\3")
        buf.write("\60\5\60\u013d\n\60\3\60\3\60\3\61\3\61\3\61\7\61\u0144")
        buf.write("\n\61\f\61\16\61\u0147\13\61\3\61\3\61\3\61\3\62\3\62")
        buf.write("\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65\3\66\3\66\7\66")
        buf.write("\u0158\n\66\f\66\16\66\u015b\13\66\3\67\3\67\3\67\3\67")
        buf.write("\3\67\38\68\u0163\n8\r8\168\u0164\38\38\39\39\39\39\5")
        buf.write("9\u016d\n9\3:\3:\3:\7:\u0172\n:\f:\16:\u0175\13:\3:\5")
        buf.write(":\u0178\n:\3:\3:\3;\3;\3;\7;\u017f\n;\f;\16;\u0182\13")
        buf.write(";\3;\3;\3;\3\u0112\2<\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\2\37\2!\20#\21%\22\'")
        buf.write("\23)\24+\25-\26/\27\61\30\63\31\65\32\67\339\34;\35=\36")
        buf.write("?\37A C!E\"G#I$K%M&O\'Q(S)U*W+Y,[\2]\2_\2a-c\2e\2g\2i")
        buf.write("\2k.m/o\60q\61s\62u\63\3\2\13\4\2\f\f\17\17\3\2\62;\4")
        buf.write("\2GGgg\6\2\n\f\16\17$$^^\t\2$$^^ddhhppttvv\5\2C\\aac|")
        buf.write("\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\4\3\f\f\17\17\2\u0190")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3")
        buf.write("\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2")
        buf.write("\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3")
        buf.write("\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E")
        buf.write("\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2")
        buf.write("O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2")
        buf.write("\2Y\3\2\2\2\2a\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2")
        buf.write("\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\3w\3\2\2\2\5}\3\2")
        buf.write("\2\2\7\u0086\3\2\2\2\t\u008a\3\2\2\2\13\u008d\3\2\2\2")
        buf.write("\r\u0093\3\2\2\2\17\u0096\3\2\2\2\21\u009b\3\2\2\2\23")
        buf.write("\u00a2\3\2\2\2\25\u00a6\3\2\2\2\27\u00ab\3\2\2\2\31\u00b3")
        buf.write("\3\2\2\2\33\u00b9\3\2\2\2\35\u00c0\3\2\2\2\37\u00c5\3")
        buf.write("\2\2\2!\u00cb\3\2\2\2#\u00ce\3\2\2\2%\u00d1\3\2\2\2\'")
        buf.write("\u00d3\3\2\2\2)\u00d5\3\2\2\2+\u00d7\3\2\2\2-\u00d9\3")
        buf.write("\2\2\2/\u00db\3\2\2\2\61\u00dd\3\2\2\2\63\u00e0\3\2\2")
        buf.write("\2\65\u00e3\3\2\2\2\67\u00e5\3\2\2\29\u00e7\3\2\2\2;\u00e9")
        buf.write("\3\2\2\2=\u00ec\3\2\2\2?\u00ef\3\2\2\2A\u00f1\3\2\2\2")
        buf.write("C\u00f3\3\2\2\2E\u00f5\3\2\2\2G\u00f7\3\2\2\2I\u00f9\3")
        buf.write("\2\2\2K\u00fb\3\2\2\2M\u00fd\3\2\2\2O\u00ff\3\2\2\2Q\u0101")
        buf.write("\3\2\2\2S\u010c\3\2\2\2U\u011c\3\2\2\2W\u011f\3\2\2\2")
        buf.write("Y\u012c\3\2\2\2[\u012e\3\2\2\2]\u0138\3\2\2\2_\u013a\3")
        buf.write("\2\2\2a\u0140\3\2\2\2c\u014b\3\2\2\2e\u014d\3\2\2\2g\u014f")
        buf.write("\3\2\2\2i\u0152\3\2\2\2k\u0155\3\2\2\2m\u015c\3\2\2\2")
        buf.write("o\u0162\3\2\2\2q\u016c\3\2\2\2s\u016e\3\2\2\2u\u017b\3")
        buf.write("\2\2\2wx\7d\2\2xy\7t\2\2yz\7g\2\2z{\7c\2\2{|\7m\2\2|\4")
        buf.write("\3\2\2\2}~\7e\2\2~\177\7q\2\2\177\u0080\7p\2\2\u0080\u0081")
        buf.write("\7v\2\2\u0081\u0082\7k\2\2\u0082\u0083\7p\2\2\u0083\u0084")
        buf.write("\7w\2\2\u0084\u0085\7g\2\2\u0085\6\3\2\2\2\u0086\u0087")
        buf.write("\7h\2\2\u0087\u0088\7q\2\2\u0088\u0089\7t\2\2\u0089\b")
        buf.write("\3\2\2\2\u008a\u008b\7f\2\2\u008b\u008c\7q\2\2\u008c\n")
        buf.write("\3\2\2\2\u008d\u008e\7y\2\2\u008e\u008f\7j\2\2\u008f\u0090")
        buf.write("\7k\2\2\u0090\u0091\7n\2\2\u0091\u0092\7g\2\2\u0092\f")
        buf.write("\3\2\2\2\u0093\u0094\7k\2\2\u0094\u0095\7h\2\2\u0095\16")
        buf.write("\3\2\2\2\u0096\u0097\7g\2\2\u0097\u0098\7n\2\2\u0098\u0099")
        buf.write("\7u\2\2\u0099\u009a\7g\2\2\u009a\20\3\2\2\2\u009b\u009c")
        buf.write("\7t\2\2\u009c\u009d\7g\2\2\u009d\u009e\7v\2\2\u009e\u009f")
        buf.write("\7w\2\2\u009f\u00a0\7t\2\2\u00a0\u00a1\7p\2\2\u00a1\22")
        buf.write("\3\2\2\2\u00a2\u00a3\7k\2\2\u00a3\u00a4\7p\2\2\u00a4\u00a5")
        buf.write("\7v\2\2\u00a5\24\3\2\2\2\u00a6\u00a7\7x\2\2\u00a7\u00a8")
        buf.write("\7q\2\2\u00a8\u00a9\7k\2\2\u00a9\u00aa\7f\2\2\u00aa\26")
        buf.write("\3\2\2\2\u00ab\u00ac\7d\2\2\u00ac\u00ad\7q\2\2\u00ad\u00ae")
        buf.write("\7q\2\2\u00ae\u00af\7n\2\2\u00af\u00b0\7g\2\2\u00b0\u00b1")
        buf.write("\7c\2\2\u00b1\u00b2\7p\2\2\u00b2\30\3\2\2\2\u00b3\u00b4")
        buf.write("\7h\2\2\u00b4\u00b5\7n\2\2\u00b5\u00b6\7q\2\2\u00b6\u00b7")
        buf.write("\7c\2\2\u00b7\u00b8\7v\2\2\u00b8\32\3\2\2\2\u00b9\u00ba")
        buf.write("\7u\2\2\u00ba\u00bb\7v\2\2\u00bb\u00bc\7t\2\2\u00bc\u00bd")
        buf.write("\7k\2\2\u00bd\u00be\7p\2\2\u00be\u00bf\7i\2\2\u00bf\34")
        buf.write("\3\2\2\2\u00c0\u00c1\7v\2\2\u00c1\u00c2\7t\2\2\u00c2\u00c3")
        buf.write("\7w\2\2\u00c3\u00c4\7g\2\2\u00c4\36\3\2\2\2\u00c5\u00c6")
        buf.write("\7h\2\2\u00c6\u00c7\7c\2\2\u00c7\u00c8\7n\2\2\u00c8\u00c9")
        buf.write("\7u\2\2\u00c9\u00ca\7g\2\2\u00ca \3\2\2\2\u00cb\u00cc")
        buf.write("\7?\2\2\u00cc\u00cd\7?\2\2\u00cd\"\3\2\2\2\u00ce\u00cf")
        buf.write("\7#\2\2\u00cf\u00d0\7?\2\2\u00d0$\3\2\2\2\u00d1\u00d2")
        buf.write("\7?\2\2\u00d2&\3\2\2\2\u00d3\u00d4\7-\2\2\u00d4(\3\2\2")
        buf.write("\2\u00d5\u00d6\7/\2\2\u00d6*\3\2\2\2\u00d7\u00d8\7,\2")
        buf.write("\2\u00d8,\3\2\2\2\u00d9\u00da\7\61\2\2\u00da.\3\2\2\2")
        buf.write("\u00db\u00dc\7\'\2\2\u00dc\60\3\2\2\2\u00dd\u00de\7(\2")
        buf.write("\2\u00de\u00df\7(\2\2\u00df\62\3\2\2\2\u00e0\u00e1\7~")
        buf.write("\2\2\u00e1\u00e2\7~\2\2\u00e2\64\3\2\2\2\u00e3\u00e4\7")
        buf.write("#\2\2\u00e4\66\3\2\2\2\u00e5\u00e6\7@\2\2\u00e68\3\2\2")
        buf.write("\2\u00e7\u00e8\7>\2\2\u00e8:\3\2\2\2\u00e9\u00ea\7@\2")
        buf.write("\2\u00ea\u00eb\7?\2\2\u00eb<\3\2\2\2\u00ec\u00ed\7>\2")
        buf.write("\2\u00ed\u00ee\7?\2\2\u00ee>\3\2\2\2\u00ef\u00f0\7]\2")
        buf.write("\2\u00f0@\3\2\2\2\u00f1\u00f2\7_\2\2\u00f2B\3\2\2\2\u00f3")
        buf.write("\u00f4\7*\2\2\u00f4D\3\2\2\2\u00f5\u00f6\7+\2\2\u00f6")
        buf.write("F\3\2\2\2\u00f7\u00f8\7}\2\2\u00f8H\3\2\2\2\u00f9\u00fa")
        buf.write("\7\177\2\2\u00faJ\3\2\2\2\u00fb\u00fc\7=\2\2\u00fcL\3")
        buf.write("\2\2\2\u00fd\u00fe\7.\2\2\u00feN\3\2\2\2\u00ff\u0100\7")
        buf.write("<\2\2\u0100P\3\2\2\2\u0101\u0102\7\61\2\2\u0102\u0103")
        buf.write("\7\61\2\2\u0103\u0107\3\2\2\2\u0104\u0106\n\2\2\2\u0105")
        buf.write("\u0104\3\2\2\2\u0106\u0109\3\2\2\2\u0107\u0105\3\2\2\2")
        buf.write("\u0107\u0108\3\2\2\2\u0108\u010a\3\2\2\2\u0109\u0107\3")
        buf.write("\2\2\2\u010a\u010b\b)\2\2\u010bR\3\2\2\2\u010c\u010d\7")
        buf.write("\61\2\2\u010d\u010e\7,\2\2\u010e\u0112\3\2\2\2\u010f\u0111")
        buf.write("\13\2\2\2\u0110\u010f\3\2\2\2\u0111\u0114\3\2\2\2\u0112")
        buf.write("\u0113\3\2\2\2\u0112\u0110\3\2\2\2\u0113\u0115\3\2\2\2")
        buf.write("\u0114\u0112\3\2\2\2\u0115\u0116\7,\2\2\u0116\u0117\7")
        buf.write("\61\2\2\u0117\u0118\3\2\2\2\u0118\u0119\b*\2\2\u0119T")
        buf.write("\3\2\2\2\u011a\u011d\5\35\17\2\u011b\u011d\5\37\20\2\u011c")
        buf.write("\u011a\3\2\2\2\u011c\u011b\3\2\2\2\u011dV\3\2\2\2\u011e")
        buf.write("\u0120\t\3\2\2\u011f\u011e\3\2\2\2\u0120\u0121\3\2\2\2")
        buf.write("\u0121\u011f\3\2\2\2\u0121\u0122\3\2\2\2\u0122X\3\2\2")
        buf.write("\2\u0123\u0125\5[.\2\u0124\u0126\5]/\2\u0125\u0124\3\2")
        buf.write("\2\2\u0125\u0126\3\2\2\2\u0126\u012d\3\2\2\2\u0127\u0128")
        buf.write("\5W,\2\u0128\u0129\5_\60\2\u0129\u012d\3\2\2\2\u012a\u012b")
        buf.write("\7\60\2\2\u012b\u012d\5]/\2\u012c\u0123\3\2\2\2\u012c")
        buf.write("\u0127\3\2\2\2\u012c\u012a\3\2\2\2\u012dZ\3\2\2\2\u012e")
        buf.write("\u012f\5W,\2\u012f\u0130\7\60\2\2\u0130\\\3\2\2\2\u0131")
        buf.write("\u0139\5W,\2\u0132\u0134\5W,\2\u0133\u0132\3\2\2\2\u0133")
        buf.write("\u0134\3\2\2\2\u0134\u0136\3\2\2\2\u0135\u0137\5_\60\2")
        buf.write("\u0136\u0135\3\2\2\2\u0136\u0137\3\2\2\2\u0137\u0139\3")
        buf.write("\2\2\2\u0138\u0131\3\2\2\2\u0138\u0133\3\2\2\2\u0139^")
        buf.write("\3\2\2\2\u013a\u013c\t\4\2\2\u013b\u013d\5)\25\2\u013c")
        buf.write("\u013b\3\2\2\2\u013c\u013d\3\2\2\2\u013d\u013e\3\2\2\2")
        buf.write("\u013e\u013f\5W,\2\u013f`\3\2\2\2\u0140\u0145\5c\62\2")
        buf.write("\u0141\u0144\5e\63\2\u0142\u0144\5g\64\2\u0143\u0141\3")
        buf.write("\2\2\2\u0143\u0142\3\2\2\2\u0144\u0147\3\2\2\2\u0145\u0143")
        buf.write("\3\2\2\2\u0145\u0146\3\2\2\2\u0146\u0148\3\2\2\2\u0147")
        buf.write("\u0145\3\2\2\2\u0148\u0149\5c\62\2\u0149\u014a\b\61\3")
        buf.write("\2\u014ab\3\2\2\2\u014b\u014c\7$\2\2\u014cd\3\2\2\2\u014d")
        buf.write("\u014e\n\5\2\2\u014ef\3\2\2\2\u014f\u0150\7^\2\2\u0150")
        buf.write("\u0151\t\6\2\2\u0151h\3\2\2\2\u0152\u0153\7^\2\2\u0153")
        buf.write("\u0154\n\6\2\2\u0154j\3\2\2\2\u0155\u0159\t\7\2\2\u0156")
        buf.write("\u0158\t\b\2\2\u0157\u0156\3\2\2\2\u0158\u015b\3\2\2\2")
        buf.write("\u0159\u0157\3\2\2\2\u0159\u015a\3\2\2\2\u015al\3\2\2")
        buf.write("\2\u015b\u0159\3\2\2\2\u015c\u015d\7o\2\2\u015d\u015e")
        buf.write("\7c\2\2\u015e\u015f\7k\2\2\u015f\u0160\7p\2\2\u0160n\3")
        buf.write("\2\2\2\u0161\u0163\t\t\2\2\u0162\u0161\3\2\2\2\u0163\u0164")
        buf.write("\3\2\2\2\u0164\u0162\3\2\2\2\u0164\u0165\3\2\2\2\u0165")
        buf.write("\u0166\3\2\2\2\u0166\u0167\b8\2\2\u0167p\3\2\2\2\u0168")
        buf.write("\u016d\13\2\2\2\u0169\u016a\5Y-\2\u016a\u016b\7\60\2\2")
        buf.write("\u016b\u016d\3\2\2\2\u016c\u0168\3\2\2\2\u016c\u0169\3")
        buf.write("\2\2\2\u016dr\3\2\2\2\u016e\u0173\5c\62\2\u016f\u0172")
        buf.write("\5e\63\2\u0170\u0172\5g\64\2\u0171\u016f\3\2\2\2\u0171")
        buf.write("\u0170\3\2\2\2\u0172\u0175\3\2\2\2\u0173\u0171\3\2\2\2")
        buf.write("\u0173\u0174\3\2\2\2\u0174\u0177\3\2\2\2\u0175\u0173\3")
        buf.write("\2\2\2\u0176\u0178\t\n\2\2\u0177\u0176\3\2\2\2\u0178\u0179")
        buf.write("\3\2\2\2\u0179\u017a\b:\4\2\u017at\3\2\2\2\u017b\u0180")
        buf.write("\5c\62\2\u017c\u017f\5e\63\2\u017d\u017f\5g\64\2\u017e")
        buf.write("\u017c\3\2\2\2\u017e\u017d\3\2\2\2\u017f\u0182\3\2\2\2")
        buf.write("\u0180\u017e\3\2\2\2\u0180\u0181\3\2\2\2\u0181\u0183\3")
        buf.write("\2\2\2\u0182\u0180\3\2\2\2\u0183\u0184\5i\65\2\u0184\u0185")
        buf.write("\b;\5\2\u0185v\3\2\2\2\27\2\u0107\u0112\u011c\u0121\u0125")
        buf.write("\u012c\u0133\u0136\u0138\u013c\u0143\u0145\u0159\u0164")
        buf.write("\u016c\u0171\u0173\u0177\u017e\u0180\6\b\2\2\3\61\2\3")
        buf.write(":\3\3;\4")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BREAK = 1
    CONTINUE = 2
    FOR = 3
    DO = 4
    WHILE = 5
    IF = 6
    ELSE = 7
    RETURN = 8
    INTTYPE = 9
    VOIDTYPE = 10
    BOOLEANTYPE = 11
    FLOATTYPE = 12
    STRINGTYPE = 13
    EQUAL = 14
    NOTEQUAL = 15
    ASSIGN = 16
    ADDOP = 17
    MINUSOP = 18
    MULOP = 19
    DIVOP = 20
    MODOP = 21
    AND = 22
    OR = 23
    NOT = 24
    LT = 25
    ST = 26
    LE = 27
    SE = 28
    LSB = 29
    RSB = 30
    LB = 31
    RB = 32
    LP = 33
    RP = 34
    SEMI = 35
    COMMA = 36
    COLON = 37
    LINE_COMMENT = 38
    BLOCK_COMMENT = 39
    BOOLLIT = 40
    INTLIT = 41
    FLOATLIT = 42
    STRINGLIT = 43
    ID = 44
    MAIN = 45
    WS = 46
    ERROR_CHAR = 47
    UNCLOSE_STRING = 48
    ILLEGAL_ESCAPE = 49

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'break'", "'continue'", "'for'", "'do'", "'while'", "'if'", 
            "'else'", "'return'", "'int'", "'void'", "'boolean'", "'float'", 
            "'string'", "'=='", "'!='", "'='", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'&&'", "'||'", "'!'", "'>'", "'<'", "'>='", "'<='", 
            "'['", "']'", "'('", "')'", "'{'", "'}'", "';'", "','", "':'", 
            "'main'" ]

    symbolicNames = [ "<INVALID>",
            "BREAK", "CONTINUE", "FOR", "DO", "WHILE", "IF", "ELSE", "RETURN", 
            "INTTYPE", "VOIDTYPE", "BOOLEANTYPE", "FLOATTYPE", "STRINGTYPE", 
            "EQUAL", "NOTEQUAL", "ASSIGN", "ADDOP", "MINUSOP", "MULOP", 
            "DIVOP", "MODOP", "AND", "OR", "NOT", "LT", "ST", "LE", "SE", 
            "LSB", "RSB", "LB", "RB", "LP", "RP", "SEMI", "COMMA", "COLON", 
            "LINE_COMMENT", "BLOCK_COMMENT", "BOOLLIT", "INTLIT", "FLOATLIT", 
            "STRINGLIT", "ID", "MAIN", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "BREAK", "CONTINUE", "FOR", "DO", "WHILE", "IF", "ELSE", 
                  "RETURN", "INTTYPE", "VOIDTYPE", "BOOLEANTYPE", "FLOATTYPE", 
                  "STRINGTYPE", "TRUE", "FALSE", "EQUAL", "NOTEQUAL", "ASSIGN", 
                  "ADDOP", "MINUSOP", "MULOP", "DIVOP", "MODOP", "AND", 
                  "OR", "NOT", "LT", "ST", "LE", "SE", "LSB", "RSB", "LB", 
                  "RB", "LP", "RP", "SEMI", "COMMA", "COLON", "LINE_COMMENT", 
                  "BLOCK_COMMENT", "BOOLLIT", "INTLIT", "FLOATLIT", "WP", 
                  "FP", "EXPONENT", "STRINGLIT", "DOUBLEQUOTE", "STRCHAR", 
                  "ESCAPE_SEQ", "NOT_ESCAPE_SEQ", "ID", "MAIN", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text);
        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[47] = self.STRINGLIT_action 
            actions[56] = self.UNCLOSE_STRING_action 
            actions[57] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('"',"")
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.lstrip('"').rstrip("\n\r")
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text.lstrip('"')
     


