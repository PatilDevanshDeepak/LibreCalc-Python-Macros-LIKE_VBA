import uno

class WorkBook:
	def __init__(self):
		self.doc = XSCRIPTCONTEXT.getDocument()
		self.active = self.doc.CurrentController
		self.ActiveSheet = self.getActiveSheet()
		self.ActiveCell = self.getActiveSelection()
		
	# Macro Functionalities
	def Select(self, oCell):
		self.active.select(oCell)
		self.ActiveCell = oCell.getCellByPosition(0 , 0)
		
	def getActiveSheet(self):
		return self.active.getActiveSheet()
		
	def getActiveSelection(self):
		return self.active.getSelection()
	
	def Cell(self, row, col):
		return self.ActiveSheet.getCellByPosition(col-1, row-1)
		
	def Range(self, rangeName=None , fromCell=None , toCell=None):
		if self.isRangeNameGiven(isRowIndex=fromCell , isColumnIndex=toCell , isRangeName=rangeName):
			return self.ActiveSheet.getCellRangeByName(rangeName)
		else:
			return self.ActiveSheet.getCellRangeByName(fromCell.AbsoluteName+":"+toCell.AbsoluteName)
		
	def Offset(self, rowIndex, colIndex):
		maxColumns = self.ActiveSheet.Columns.Count - 1
		maxRows = self.ActiveSheet.Rows.Count - 1
		newRow = self.ActiveCell.RangeAddress.StartRow + rowIndex
		newCol = self.ActiveCell.RangeAddress.StartColumn + colIndex
		newRow = max(0, min(newRow, maxRows))
		newCol = max(0, min(newCol, maxColumns))
		return self.ActiveSheet.getCellByPosition(newCol, newRow)
		
	def Row(self, oCell):
		return 	oCell.RangeAddress.StartRow + 1
	
	def Column(self, oCell):
		return oCell.RangeAddress.StartColumn + 1

	# Funtions for workbook class development
	def isRangeNameGiven(self, isRowIndex=None , isColumnIndex=None , isRangeName=None):
		if isRangeName!=None and (isRowIndex==None and isColumnIndex==None):
			return True
		elif isRangeName==None and (isRowIndex!=None and isColumnIndex!=None):
			return False

	def isNull(self, oCell):
		return True if len(oCell.getString())==0 else False



Calc = WorkBook()

def Automate():
	Calc.Select(Calc.Range("A1"))
	Calc.setString("Hello World")
