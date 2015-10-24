from PyQt4.QtGui import *
from PyQt4.QtCore import *


class MyHighlighter(QSyntaxHighlighter):
    def __init__(self, parent, theme):
        QSyntaxHighlighter.__init__(self, parent)
        self.parent = parent
        keyword = QTextCharFormat()
        reservedClasses = QTextCharFormat()
        assignmentOperator = QTextCharFormat()
        delimiter = QTextCharFormat()
        specialConstant = QTextCharFormat()
        boolean = QTextCharFormat()
        number = QTextCharFormat()
        comment = QTextCharFormat()
        string = QTextCharFormat()
        singleQuotedString = QTextCharFormat()

        self.highlightingRules = []

        # keyword
        brush = QBrush(QColor('#cb7730'), Qt.SolidPattern)
        keyword.setForeground(brush)
        keyword.setFontWeight(QFont.Bold)
        keywords = QStringList([
            'and', 'assert', 'break', 'class', 'continue', 'def',
            'del', 'elif', 'else', 'except', 'exec', 'finally',
            'for', 'from', 'global', 'if', 'import', 'in',
            'is', 'lambda', 'not', 'or', 'pass', 'print',
            'raise', 'return', 'try', 'while', 'yield',
            'None', 'True', 'False', ])

        for word in keywords:
            pattern = QRegExp("\\b" + word + "\\b")
            rule = HighlightingRule(pattern, keyword)
            self.highlightingRules.append(rule)

        # reservedClasses
        brush = QBrush(QColor('#8888c6'), Qt.SolidPattern)
        reservedClasses.setForeground(brush)
        reservedClasses.setFontWeight(QFont.Bold)
        keywords = QStringList(["str", "int", "bool", "float", "range", "xrange"])
        for word in keywords:
            pattern = QRegExp("\\b" + word + "\\b")
            rule = HighlightingRule(pattern, reservedClasses)
            self.highlightingRules.append(rule)

        # output
        brush = QBrush(Qt.magenta, Qt.SolidPattern)
        specialConstant.setForeground(brush)
        keywords = QStringList(["printf", ])
        for word in keywords:
            pattern = QRegExp("\\b" + word + "\\b")
            rule = HighlightingRule(pattern, specialConstant)
            self.highlightingRules.append(rule)

        # boolean
        brush = QBrush(QColor('#8888c6'), Qt.SolidPattern)
        boolean.setForeground(brush)
        keywords = QStringList(["True", "False"])
        for word in keywords:
            pattern = QRegExp("\\b" + word + "\\b")
            rule = HighlightingRule(pattern, boolean)
            self.highlightingRules.append(rule)

        # number
        brush = QBrush(QColor('#8888c6'), Qt.SolidPattern)
        pattern = QRegExp("[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?")
        pattern.setMinimal(True)
        number.setForeground(brush)
        rule = HighlightingRule(pattern, number)
        self.highlightingRules.append(rule)

        # comment
        brush = QBrush(QColor('#808080'), Qt.SolidPattern)
        pattern = QRegExp("#[^\n]*")
        comment.setForeground(brush)
        rule = HighlightingRule(pattern, comment)
        self.highlightingRules.append(rule)

        # string
        brush = QBrush(QColor('#a5c261'), Qt.SolidPattern)
        pattern = QRegExp("\".*\"")
        pattern.setMinimal(True)
        string.setForeground(brush)
        rule = HighlightingRule(pattern, string)
        self.highlightingRules.append(rule)

        # singleQuotedString
        pattern = QRegExp("\'.*\'")
        pattern.setMinimal(True)
        singleQuotedString.setForeground(brush)
        rule = HighlightingRule(pattern, singleQuotedString)
        self.highlightingRules.append(rule)

    def highlightBlock(self, text):
        for rule in self.highlightingRules:
            expression = QRegExp(rule.pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, rule.format)
                index = text.indexOf(expression, index + length)
        self.setCurrentBlockState(0)


class HighlightingRule():
    def __init__(self, pattern, format):
        self.pattern = pattern
        self.format = format

