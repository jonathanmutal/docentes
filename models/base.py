from odoo.exceptions import ValidationError, UserError


class Base:
    """
    Class base to search and create new object from a class.
    :env: is the enviroment for the class, for example in docente.aportes is 
          env['docentes.aportes']
    """
    def __init__(self, env):
        self.env = env

    def get(self, vals):
        conditions = []
        for field, value in vals.items():
            conditions.append((field, '=', value))
        self.obj = self.env.search(conditions)
        return self.obj or {}

    def get_create(self, objeto_dic, **args):
        obj = self.get(objeto_dic)
        if not obj:
            obj = objeto_dic
            for field, value in args.items():
                objeto_dic[field] = value
            self.obj = self.create(vals=obj)
        return self.obj

    def create(self, vals):
        self.obj = self.env.create(vals)
        return self.obj

    def remove(self):
        self.obj.unlink()
