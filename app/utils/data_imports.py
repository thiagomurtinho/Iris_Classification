def data_extraction_row_value(DataFrame, DataCompare, ColumName):
  data = []

  for item in DataFrame.itertuples(index=False, name='Iris'):
    for DataCompare in item:
      if(ColumName == 'SepalLengthCm'):
        data.append(item.SepalLengthCm)
      if(ColumName == 'SepalWidthCm'):
        data.append(item.SepalWidthCm)
      if(ColumName == 'PetalWidthCm'):
        data.append(item.PetalWidthCm)
      if(ColumName == 'PetalLengthCm'):
        data.append(item.PetalLengthCm)

  return data