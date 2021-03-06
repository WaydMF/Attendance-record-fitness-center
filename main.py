import sys
import sqlite3
from datetime import *
# Импортируем наш интерфейс
from laba2 import *
from visitors import *
from groups import *
from statusGr import *
from authorization import *
from checkDB import *
from PyQt5 import QtCore, QtGui, QtWidgets


def readdb(request=None):
    conn = sqlite3.connect('Visitors.sqlite')
    cursor = conn.cursor()
    cursor.execute(request)
    result = cursor.fetchall()
    return result


def changedb(request=None):
    conn = sqlite3.connect('Visitors.sqlite')
    cursor = conn.cursor()
    cursor.execute(f'{request}')
    conn.commit()


class AuthorizationWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Authorization()
        self.ui.setupUi(self)

        self.ui.pushButtonEnter.clicked.connect(self.enter)

    def enter(self):
        if self.ui.lineEditLogin.text() == 'admin':
            if self.ui.lineEditPassword.text() == 'pass':
                myapp.ui.lineEditUser.setText('admin')
                myapp.show()
                self.close()
            else:
                self.ui.lineEditPassword.clear()
                message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, 'Ошибка', f'Неверный пароль')
                message.exec_()
        else:
            myapp.ui.lineEditUser.setText(self.ui.lineEditLogin.text())
            myapp.ui.actionCheckDB.setVisible(0)
            myapp.ui.actionSaveLog.setVisible(0)
            myapp.show()
            self.close()


class CheckDBWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_CheckDB()
        self.ui.setupUi(self)

        self.ui.pushButtonGroups.clicked.connect(self.groups)
        self.ui.pushButtonVisitors.clicked.connect(self.visitors)
        self.ui.pushButtonLessons.clicked.connect(self.lessons)
        self.ui.pushButtonBack.clicked.connect(self.back)

        self.ui.tableGroups.hide()
        self.ui.tableVisitors.hide()
        self.ui.tableLessons.hide()

    def groups(self):
        self.ui.tableGroups.show()
        self.ui.tableLessons.hide()
        self.ui.tableVisitors.hide()

        info = readdb(f'SELECT * FROM groups')
        self.ui.tableGroups.setRowCount(len(info))
        self.ui.tableGroups.horizontalHeader()
        self.ui.tableGroups.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        for i, row in enumerate(info):
            for j, val in enumerate(row):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
                item.setText(str(val))
                self.ui.tableGroups.setItem(i, j, item)

    def visitors(self):
        self.ui.tableVisitors.show()
        self.ui.tableGroups.hide()
        self.ui.tableLessons.hide()

        info = readdb(f'SELECT * FROM visitors')
        self.ui.tableVisitors.setRowCount(len(info))
        self.ui.tableVisitors.horizontalHeader()
        self.ui.tableVisitors.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        for i, row in enumerate(info):
            for j, val in enumerate(row):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
                item.setText(str(val))
                self.ui.tableVisitors.setItem(i, j, item)

    def lessons(self):
        self.ui.tableLessons.show()
        self.ui.tableGroups.hide()
        self.ui.tableVisitors.hide()

        info = readdb(f'SELECT * FROM lessons')
        self.ui.tableLessons.setRowCount(len(info))
        self.ui.tableLessons.horizontalHeader()
        self.ui.tableLessons.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        for i, row in enumerate(info):
            for j, val in enumerate(row):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
                item.setText(str(val))
                self.ui.tableLessons.setItem(i, j, item)

    def back(self):
        self.close()


class StatusGrWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_StatusGroup()
        self.ui.setupUi(self)

        self.ui.pushButtonBack.clicked.connect(self.back)

        text = []
        group = myapp.ui.comboBoxGroups.currentText()
        result = readdb(f'SELECT * FROM visitors')
        for row in result:
            if group == row[4]:
                if row[2] == 0:
                    text.append(f'{row[1]} не имеет посещений. Занятий посещено: {row[3]}.')
                elif row[2] == 1:
                    text.append(f'{row[1]} имеет {row[2]} посещение. Занятий посещено: {row[3]}.')
                elif 1 < row[2] < 5:
                    text.append(f'{row[1]} имеет {row[2]} посещения. Занятий посещено: {row[3]}.')
                elif row[2] >= 5:
                    text.append(f'{row[1]} имеет {row[2]} посещений. Занятий посещено: {row[3]}.')
        self.ui.textEdit.setPlainText('\n'.join(text))

    def back(self):
        self.close()


class GroupsWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Groups()
        self.ui.setupUi(self)

        self.ui.pushButtonBack.clicked.connect(self.back)
        self.ui.comboBoxGroups.addItems(myapp.groups)
        self.ui.pushButtonAdd.clicked.connect(self.add)
        self.ui.pushButtonDelete.clicked.connect(self.delete)

    def add(self):
        if self.ui.lineEdit.text().isalpha():
            changedb(f'INSERT INTO groups VALUES(\'{self.ui.lineEdit.text()}\', 0, 0)')
            myapp.groups = [i[0] for i in readdb(f'SELECT * FROM groups')]
            self.ui.comboBoxGroups.clear()
            self.ui.comboBoxGroups.addItems(myapp.groups)
            myapp.ui.comboBoxGroups.clear()
            myapp.ui.comboBoxGroups.addItems(myapp.groups)
        else:
            message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, 'Ошибка',
                                            'Название группы может содержать только буквы\n'
                                            '         и должно состоять из одного слова')
            message.exec_()
        myapp.log.append(f'Добавлена новая группа: {self.ui.lineEdit.text()}')

    def delete(self):
        group = self.ui.comboBoxGroups.currentText()
        changedb(f'DELETE FROM groups WHERE name = \'{group}\'')
        changedb(f'UPDATE visitors SET gruppa = NULL WHERE gruppa = \'{group}\'')
        myapp.groups = [i[0] for i in readdb(f'SELECT * FROM groups')]
        self.ui.comboBoxGroups.clear()
        self.ui.comboBoxGroups.addItems(myapp.groups)
        myapp.ui.comboBoxGroups.clear()
        myapp.ui.comboBoxGroups.addItems(myapp.groups)
        myapp.log.append(f'Удалена группа: {group}')

    def back(self):
        self.close()


class VisitorsWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):              # ПОВТОРЯЮЩИЕСЯ ИМЕНА
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Visitors()
        self.ui.setupUi(self)

        wgvisitors = readdb(f'SELECT * FROM visitors WHERE gruppa is NULL')  # visitors without group
        for visitor in wgvisitors:
            self.ui.comboBoxVisitors.addItem(visitor[1])
        self.ui.comboBoxVisitors.addItem('Новый посетитель')

        nfgroups = readdb(f'SELECT * FROM groups WHERE quantityvisitors < 6')
        for group in nfgroups:
            self.ui.comboBoxGroups.addItem(group[0])

        groups1 = readdb(f'SELECT name FROM groups WHERE quantityvisitors > 0')  # groups with >=1 people
        for group in groups1:
            self.ui.comboBoxGroups_2.addItem(group[0])

        self.ui.radioButton.setChecked(True)
        self.ui.button_group = QtWidgets.QButtonGroup()
        self.ui.button_group.addButton(self.ui.radioButton)
        self.ui.button_group.addButton(self.ui.radioButton_2)
        self.ui.comboBoxVisitors.activated.connect(self.combo_visitors)
        self.ui.comboBoxGroups_2.activated.connect(self.combo_groups_2)
        self.ui.pushButtonAdd.clicked.connect(self.add)
        self.ui.pushButtonLeaveGroup.clicked.connect(self.leave_group)
        self.ui.pushButtonDeleteVisitor.clicked.connect(self.delete_visitor)
        self.ui.pushButtonBack.clicked.connect(self.back)

        self.ui.lineEdit.hide()
        self.ui.radioButton.hide()
        self.ui.radioButton_2.hide()

    def combo_visitors(self):
        if self.ui.comboBoxVisitors.currentText() == 'Новый посетитель':
            self.ui.lineEdit.show()
            self.ui.radioButton.show()
            self.ui.radioButton_2.show()
        else:
            self.ui.lineEdit.hide()
            self.ui.radioButton.hide()
            self.ui.radioButton_2.hide()

    def combo_groups_2(self):
        group = self.ui.comboBoxGroups_2.currentText()
        listgroup = []
        namesvisitors = []
        result = readdb(f'SELECT * FROM visitors')
        for row in result:
            if group == row[4]:
                listgroup.append(row)
        for info in listgroup:
            namesvisitors.append(info[1])
        self.ui.comboBoxVisitors_2.clear()
        self.ui.comboBoxVisitors_2.addItems(namesvisitors)

    def add(self):
        if readdb(f'SELECT quantityvisitors FROM groups '
                  f'WHERE name = \'{self.ui.comboBoxGroups.currentText()}\'')[0][0] < 6:
            changedb(f'UPDATE groups SET quantityvisitors = quantityvisitors + 1 '
                     f'WHERE name = \'{self.ui.comboBoxGroups.currentText()}\'')
            idsvisitors = str(
                readdb(f'SELECT idsvisitors FROM groups WHERE name = \'{self.ui.comboBoxGroups.currentText()}\'')[0][0])
            if self.ui.comboBoxVisitors.currentText() == 'Новый посетитель':
                idnewvisitor = readdb(f'SELECT count(*) FROM visitors')[0][0] + 1
                checkbutton = self.ui.radioButton.isChecked()
                if checkbutton is True:
                    changedb(f'INSERT INTO visitors VALUES({idnewvisitor}, \'{self.ui.lineEdit.text()}\', '
                             f'8, 0, \'{self.ui.comboBoxGroups.currentText()}\')')
                    myapp.log.append(f'В группу {self.ui.comboBoxGroups.currentText()} добавлен новый посетитель '
                                     f'с абонементом на 8 посещений: {self.ui.lineEdit.text()}')
                else:
                    changedb(f'INSERT INTO visitors VALUES({idnewvisitor}, \'{self.ui.lineEdit.text()}\', '
                             f'16, 0, \'{self.ui.comboBoxGroups.currentText().currentText()}\')')
                    myapp.log.append(f'В группу {self.ui.comboBoxGroups} добавлен новый посетитель '
                                     f'с абонементом на 16 посещений: {self.ui.lineEdit.text()}')
                if idsvisitors == '0':
                    changedb(f'UPDATE groups SET idsvisitors = \'{idnewvisitor}\' '
                             f'WHERE name = \'{self.ui.comboBoxGroups.currentText()}\'')
                else:
                    idsvisitors = idsvisitors + ',' + str(idnewvisitor)
                    changedb(
                        f'UPDATE groups SET idsvisitors = \'{idsvisitors }\' '
                        f'WHERE name = \'{self.ui.comboBoxGroups.currentText()}\'')
                self.ui.lineEdit.hide()
                self.ui.radioButton.hide()
                self.ui.radioButton_2.hide()
            else:
                idvisitor = readdb(f'SELECT id FROM visitors '
                                   f'WHERE name = \'{self.ui.comboBoxVisitors.currentText()}\'')[0][0]
                idsvisitors = idsvisitors + ',' + str(idvisitor)
                changedb(f'UPDATE visitors SET gruppa = \'{self.ui.comboBoxGroups.currentText()}\' '
                         f'WHERE name = \'{self.ui.comboBoxVisitors.currentText()}\'')
                changedb(f'UPDATE groups SET idsvisitors = \'{idsvisitors }\' '
                         f'WHERE name = \'{self.ui.comboBoxGroups.currentText()}\'')
                myapp.log.append(f'Посетитель {self.ui.comboBoxVisitors.currentText()} '
                                 f'добавлен в группу "{self.ui.comboBoxGroups.currentText()}"')

            self.ui.lineEdit.clear()
            wgvisitors = readdb(f'SELECT * FROM visitors WHERE gruppa is NULL')  # visitors without group
            self.ui.comboBoxVisitors.clear()
            for visitor in wgvisitors:
                self.ui.comboBoxVisitors.addItem(visitor[1])
            self.ui.comboBoxVisitors.addItem('Новый посетитель')
            self.ui.comboBoxGroups_2.clear()
            groups1 = readdb(f'SELECT name FROM groups WHERE quantityvisitors > 0')  # groups with >=1 people
            for group in groups1:
                self.ui.comboBoxGroups_2.addItem(group[0])
            self.ui.comboBoxVisitors_2.clear()

            self.ui.comboBoxGroups.clear()
            nfgroups = readdb(f'SELECT * FROM groups WHERE quantityvisitors < 6')
            for group in nfgroups:
                self.ui.comboBoxGroups.addItem(group[0])

    def leave_group(self):
        if self.ui.comboBoxVisitors_2.currentText() != '':
            idvisitor = readdb(f'SELECT id FROM visitors WHERE name = \'{self.ui.comboBoxVisitors_2.currentText()}\'')[0][0]
            group = readdb(f'SELECT gruppa FROM visitors WHERE name = \'{self.ui.comboBoxVisitors_2.currentText()}\'')[0][0]
            changedb(f'UPDATE visitors SET gruppa = NULL WHERE name = \'{self.ui.comboBoxVisitors_2.currentText()}\'')
            changedb(f'UPDATE groups SET quantityvisitors = quantityvisitors - 1 WHERE name = \'{group}\'')
            idsvisitors = readdb(f'SELECT idsvisitors FROM groups WHERE name = \'{group}\'')[0][0]
            idsvisitors = idsvisitors.split(',')
            idvisitor = idsvisitors.index(str(idvisitor))
            idsvisitors.pop(idvisitor)
            idsvisitors = ','.join(idsvisitors)
            changedb(f'UPDATE groups SET idsvisitors = \'{idsvisitors}\' WHERE name = \'{group}\'')

            wgvisitors = readdb(f'SELECT * FROM visitors WHERE gruppa is NULL')  # visitors without group
            self.ui.comboBoxVisitors.clear()
            for visitor in wgvisitors:
                self.ui.comboBoxVisitors.addItem(visitor[1])
            self.ui.comboBoxVisitors.addItem('Новый посетитель')
            self.ui.comboBoxGroups_2.clear()
            groups1 = readdb(f'SELECT name FROM groups WHERE quantityvisitors > 0')  # groups with >=1 people
            for group in groups1:
                self.ui.comboBoxGroups_2.addItem(group[0])
            myapp.log.append(f'Посетитель {self.ui.comboBoxVisitors_2.currentText()} '
                             f'вышел из группы "{self.ui.comboBoxGroups_2.currentText()}"')
            self.ui.comboBoxVisitors_2.clear()

            self.ui.comboBoxGroups.clear()
            nfgroups = readdb(f'SELECT * FROM groups WHERE quantityvisitors < 6')
            for group in nfgroups:
                self.ui.comboBoxGroups.addItem(group[0])

    def delete_visitor(self):
        if self.ui.comboBoxVisitors_2.currentText() != '':
            idvisitor = readdb(f'SELECT id FROM visitors WHERE name = \'{self.ui.comboBoxVisitors_2.currentText()}\'')[0][0]
            group = readdb(f'SELECT gruppa FROM visitors WHERE name = \'{self.ui.comboBoxVisitors_2.currentText()}\'')[0][0]
            changedb(f'DELETE FROM visitors WHERE name = \'{self.ui.comboBoxVisitors_2.currentText()}\'')
            changedb(f'UPDATE groups SET quantityvisitors = quantityvisitors -1 WHERE name = \'{group}\'')
            idsvisitors = readdb(f'SELECT idsvisitors FROM groups WHERE name = \'{group}\'')[0][0]
            idsvisitors = idsvisitors.split(',')
            idvisitor = idsvisitors.index(str(idvisitor))
            idsvisitors.pop(idvisitor)
            idsvisitors = ','.join(idsvisitors)
            changedb(f'UPDATE groups SET idsvisitors = \'{idsvisitors}\' WHERE name = \'{group}\'')
            myapp.log.append(f'Посетитель {self.ui.comboBoxVisitors_2.currentText()} '
                             f'вышел из группы "{group}"')
            myapp.log.append(f'Посетитель {self.ui.comboBoxVisitors_2.currentText()} '
                             f'удален их системы')

            wgvisitors = readdb(f'SELECT * FROM visitors WHERE gruppa is NULL')  # visitors without group
            self.ui.comboBoxVisitors.clear()
            for visitor in wgvisitors:
                self.ui.comboBoxVisitors.addItem(visitor[1])
            self.ui.comboBoxVisitors.addItem('Новый посетитель')
            self.ui.comboBoxGroups_2.clear()
            groups1 = readdb(f'SELECT name FROM groups WHERE quantityvisitors > 0')  # groups with >=1 people
            for group in groups1:
                self.ui.comboBoxGroups_2.addItem(group[0])
            self.ui.comboBoxVisitors_2.clear()

            self.ui.comboBoxGroups.clear()
            nfgroups = readdb(f'SELECT * FROM groups WHERE quantityvisitors < 6')
            for group in nfgroups:
                self.ui.comboBoxGroups.addItem(group[0])

    def back(self):
        self.close()


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.groups = [i[0] for i in readdb(f'SELECT * FROM groups')]

        self.ui.actionGroups.triggered.connect(self.groups_window)
        self.ui.actionVisitors.triggered.connect(self.visitors_window)
        self.ui.actionStatusGr.triggered.connect(self.status_window)
        self.ui.actionSaveLog.triggered.connect(self.save_log)
        self.ui.actionCheckDB.triggered.connect(self.checkDB)
        self.ui.actionHelp.triggered.connect(self.help)
        self.ui.actionAboutProgramm.triggered.connect(self.about_programm)
        self.ui.actionAboutAuthor.triggered.connect(self.about_author)

        self.ui.comboBoxGroups.addItems(self.groups)
        self.ui.comboBoxGroups.activated.connect(self.combo_groups)
        self.combo_groups()
        self.ui.pushButtonTraining.clicked.connect(self.lets_train)
        self.ui.pushButtonAbsent.clicked.connect(self.absent)
        self.ui.pushButtonSubscribtion.clicked.connect(self.more_lessons)

        self.ui.radioButton.setChecked(True)
        self.ui.button_group = QtWidgets.QButtonGroup()
        self.ui.button_group.addButton(self.ui.radioButton)
        self.ui.button_group.addButton(self.ui.radioButton_2)

        self.log = []

        self.authorization_window()

    def authorization_window(self):
        self.hide()
        self.AuthorizationW = AuthorizationWindow()
        self.AuthorizationW.show()

    def groups_window(self):
        self.GroupsW = GroupsWindow()
        self.GroupsW.show()

    def visitors_window(self):
        self.VisitorsW = VisitorsWindow()
        self.VisitorsW.show()

    def status_window(self):
        if self.ui.comboBoxVisitors.currentText() != '':
            self.StatusGrW = StatusGrWindow()
            self.StatusGrW.show()

    def checkDB(self):
        self.CheckDBW = CheckDBWindow()
        self.CheckDBW.show()

    def save_log(self):
        if len(self.log) > 0:
            path, _ = QtWidgets.QFileDialog.getSaveFileName()
            k = path[::-1].find('/')
            dot = path[-k:].find('.')
            if dot == -1:
                path = f'{path}.txt'
            f = open(path, 'w', encoding='UTF8')
            for line in self.log:
                newline = f'{str(datetime.today())[:-7]} {line}'
            for line in self.log[:-1]:
                f.write("%s\n" % line)
            f.write("%s" % self.log[-1])
            f.close()

    @staticmethod
    def help():
        message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, 'Помощь',
                                        'Не имею понятия, что сюда можно написать, вроде всё понятно...')
        message.exec_()

    @staticmethod
    def about_programm():
        message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, 'О программе',
                                        'Система отслеживания посещения занятий фитнесс - центра v2.0')
        message.exec_()

    @staticmethod
    def about_author():
        message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, 'О программе',
                                        ('Я, Шукелович Александр Дмитриевич, разработал данную \n'
                                         '  программу в качестве своей лабораторной работы.'))
        message.exec_()

    def combo_groups(self):
        group = self.ui.comboBoxGroups.currentText()
        listgroup = []
        namesvisitors = []
        result = readdb(f'SELECT * FROM visitors')
        for row in result:
            if group == row[4]:
                listgroup.append(row)
        for info in listgroup:
            namesvisitors.append(info[1])
        self.ui.comboBoxVisitors.clear()
        self.ui.comboBoxVisitors.addItems(namesvisitors)
        self.ui.textEdit.clear()

    def absent(self):
        visitor = self.ui.comboBoxVisitors.currentText()
        checkbox = self.ui.checkBoxRCause.checkState()
        text = self.ui.textEdit.toPlainText().split('\n')

        if f'{visitor} отсутствует по уважительной причине.' or f'{visitor} отсутствует без уважительной причины.' \
                in self.ui.textEdit.toPlainText():
            for n, line in enumerate(text):
                if visitor in line:
                    text.pop(n)
            self.ui.textEdit.clear()
            for line in text:
                self.ui.textEdit.append(line)
        if checkbox == 2:
            self.ui.textEdit.append(f'{visitor} отсутствует по уважительной причине.')
            self.ui.checkBoxRCause.setCheckState(0)
        else:
            self.ui.textEdit.append(f'{visitor} отсутствует без уважительной причины.')

    def more_lessons(self):
        visitor = self.ui.comboBoxVisitors.currentText()
        checkbutton = self.ui.radioButton.isChecked()
        for row in readdb(f'SELECT * FROM visitors'):
            if row[1] == visitor:
                if checkbutton is True:
                    changedb(f'UPDATE visitors SET abonement = {row[2] + 8} WHERE name = \'{visitor}\'')
                    self.ui.textEdit.append(f'{visitor} приобрел(-ла) 8 занятий.')
                else:
                    changedb(f'UPDATE visitors SET abonement = {row[2] + 16} WHERE name = \'{visitor}\'')
                    self.ui.textEdit.append(f'{visitor} приобрел(-ла) 16 занятий.')

    def lets_train(self):
        text = self.ui.textEdit.toPlainText().split('\n')
        list_visitors = [i[0] for i in readdb(f'SELECT name FROM visitors '
                                              f'WHERE gruppa = "{self.ui.comboBoxGroups.currentText()}"')]
        abonements = [i[0] for i in readdb(f'SELECT abonement FROM visitors '
                                           f'WHERE gruppa = "{self.ui.comboBoxGroups.currentText()}"')]
        absents = []
        idsvisitors = []

        for line in text:
            ar = line.find(' отсутствует по уважительной причине.')
            if ar != -1:
                absent = line[:ar]
                absents.append(absent)
                i = list_visitors.index(absent)
                list_visitors.pop(i)
                abonements.pop(i)
            a = line.find(' отсутствует без уважительной причины.')
            if a != -1:
                absent = line[:a]
                i = list_visitors.index(absent)
                if abonements[i] == 0:
                    absents.append(absent)
                    list_visitors.pop(i)
                    abonements.pop(i)
        for n, i in enumerate(abonements):
            if i == 0:
                message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, 'Упс', f'{list_visitors[n]} не имеет '
                                                f'больше посещений')
                message.exec_()
                return
        d = dict(zip(list_visitors, abonements))
        for name in list_visitors:
            ids = readdb(f'SELECT id FROM visitors WHERE name == "{name}"')[0][0]
            idsvisitors.append(str(ids))
        idsvisitors = ','.join(idsvisitors)
        for key in d:
            changedb(f'UPDATE visitors SET abonement = "{d[key] - 1}" WHERE name = "{key}"')
            changedb(f'UPDATE visitors SET lessons = lessons + 1 WHERE name = "{key}"')
        changedb(f'INSERT INTO lessons '
                 f'VALUES("{str(datetime.today())[:-7]}", "{self.ui.comboBoxGroups.currentText()}",'
                 f' {len(list_visitors)}, "{idsvisitors}")')
        self.log.append(f'Проведено занятие с группой "{self.ui.comboBoxGroups.currentText()}. "'
                        f'Отсутствовали: {",".join(absents)}')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    sys.exit(app.exec_())