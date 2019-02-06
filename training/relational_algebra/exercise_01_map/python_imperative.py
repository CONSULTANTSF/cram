def python_imperative(sequence):
    raise NotImplementedError()

# def python_imperative(sequence):
#     import decimal

#     output = []
#     for row in sequence:
#         row_ = dict(row)
#         with decimal.localcontext() as dctx:
#             dctx.prec = 28
#             price_per_unit = row['price_total_quantity'] / row['quantity']
#             price_per_unit = price_per_unit.quantize(decimal.Decimal('0.0001')).normalize()
#         row_['price_per_unit'] = price_per_unit
#         output.append(row_)
#     return output
