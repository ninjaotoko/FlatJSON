# -*- coding:utf-8 -*-
# 
# Funciones utiles
#

class FlatJSON(object):
    """
    Devuelve un JSON de una sola dimensión.
    Si always_string está activo devuelve todos os valores como string, 
    incluso los int, float.

    {
        "nombre": "Pepe",
        "apellido": "Argento",
        "hijos": [
            {
                "nombre": "Coki",
                "edad": 25
            },
            {
                "nombre": "Paola",
                "edad": 22
            }
        ],
        "esposa": {
            "nombre": "Moni",
            "pasatiempos": [
                "mirar tele",
                "boludear"
            ],
            "skills": {
                "fisico": "boobies",
                "carisma": [
                    "alegre", "va al frente"
                ]
            }
        }
    }

    transforma a:


    {
        "nombre": "Pepe",
        "apellido": "Argento",
        "hijos_0_nombre": "Coki",
        "hijos_0_edad": 25,
        "hijos_1_nombre": "Paola",
        "hijos_1_edad": 22
    }    
    """

    always_string = False
    key_separator = '__'

    def __init__(self, always_string=False, key_separator='__'):
        self.always_string = always_string
        self.key_separator = key_separator

    def convert(self, data):
        datason = {}

        for key, val in data.iteritems():

            if isinstance(val, str):
                datason.update({key: val})

            elif isinstance(val, (int, float)) and self.always_string:
                datason.update({key: "{0}".format(val)})

            elif isinstance(val, (tuple, list)):

                for i, v in enumerate(val):

                    if isinstance(v, dict):
                        subdata = self.convert(v)
                        for subkey, subval in subdata.iteritems():
                            datason.update({
                                "{0}{separator}{1}{separator}{2}".format(
                                    key, i, subkey, separator=self.key_separator
                                    ): subval
                                })

                    elif isinstance(v, (list, tuple)):
                        for subi, subv in enumerate(v):
                            datason.update({
                                "{0}{separator}{1}{separator}{2}".format(
                                    key, i, subi, separator=self.key_separator
                                    ): subv
                                })

                    else:
                        datason.update({"{0}{separator}{1}".format(
                            key, i, separator=self.key_separator
                            ): v})

            elif isinstance(val, dict):

                for k, v in val.iteritems():

                    if isinstance(v, dict):
                        subdata = self.convert(v)
                        for subkey, subval in subdata.iteritems():
                            datason.update({
                                "{0}{separator}{1}{separator}{2}".format(
                                    key, k, subkey, separator=self.key_separator
                                    ): subval
                                })

                    elif isinstance(v, (list, tuple)):
                        for subi, subv in enumerate(v):
                            datason.update({
                                "{0}{separator}{1}{separator}{2}".format(
                                    key, k, subi, separator=self.key_separator
                                    ): subv})

                    else:
                        datason.update({"{0}{separator}{1}".format(
                            key, k, separator=self.key_separator
                            ): v})

            else:
                datason.update({key: val})

        return datason
