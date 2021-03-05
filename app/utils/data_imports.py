def extraction_colunms_value(DataFrame, DataCompare, ColumName):
  data = []
  index = DataFrame.Species.str.contains(DataCompare)

  if(ColumName == 'SepalLengthCm'):
    data = DataFrame[index].SepalLengthCm
  if(ColumName == 'SepalWidthCm'):
    data = DataFrame[index].SepalWidthCm
  if(ColumName == 'PetalWidthCm'):
    data = DataFrame[index].PetalWidthCm
  if(ColumName == 'PetalLengthCm'):
    data = DataFrame[index].PetalLengthCm

  return data