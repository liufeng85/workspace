class ReadTestdata():
    
    def get_step_data(self,sheet,col_numbers,action_col_num,value_col_num):
        action_data   =[]
        value_data    =[]
        for t in col_numbers:
            action_data.append(sheet.cell(t,action_col_num).value)
            value_data.append(sheet.cell(t,value_col_num).value)
        return action_data,value_data