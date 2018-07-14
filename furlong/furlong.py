class Furlong(object):
    conversion_table = {
            'inches'    : ('centimeters', 2.54),
            'feet'      : ('inches', 12)
    }
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.unit = key
            self.value = value

        self._init_forward_map()
        self._init_backward_map()

    def _init_forward_map(self):
        for base, conv in Furlong.conversion_table.items():
            func_name, conv_value = Furlong.conversion_table[base]
            func_name = "as" + func_name.title()
            setattr(self, func_name, self._make_convertor( conv_value ))

    def _init_backward_map(self):
        for func_name, base_block in Furlong.conversion_table.items():
            base_name = base_block[0]
            conv_value = 1 / base_block[1] #inverse
            func_name = "as" + func_name.title()
            setattr(self, func_name, self._make_convertor( conv_value ))


    def _make_convertor(self, conv_value):
        def _convertor():
            return self.value * conv_value
        
        return _convertor