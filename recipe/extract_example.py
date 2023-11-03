from fractions import Fraction
from typing import List
from pint import UnitRegistry

def number_str_to_float(amount_str:str)->(any,bool):
    success=False
    number_as_float=amount_str
    try:
        number_as_float=float(sum(Fraction(s)for s in f"{amount_str}".split()))
    except:
        pass
    if isinstance(number_as_float, float):
        success=True
    return number_as_float,success

extracted={"results":["1 proud chicken breasts cut into bite"]}

og=extracted['original']
def parse_paragraph_to_recipe_line(paragraph):
    paragraph=paragraph.replace("\n", " ").replace("\f", " ").replace("\t"," ")
    results=[]
    current_str=""
    for line in paragraph.split(" "):
        val, success = number_str_to_float(line)
        if success:
            # print(line,val)
            if current_str != "":
                results.append(current_str.strip())
            current_str = f"{line}"
        else:
            current_str += f"{line}"
    return results


def convert_to_qty_units(results:list[str]):
    ureg=UnitRegistry()
    dataset={}
    for i, x in enumerate(results):
        words=x.split(" ")
        qty=None
        qty_raw=None
        other=[]
        for word in words:
            print(word)
            val,success=number_str_to_float(word)
            if success:
                qty=val
                qty_raw=word
                continue
            iter_unit=None
            try:
                #item_unit=str(ureg[word].units)
                item_unit = str(ureg[word].lower().units)
            except:
                pass
            if units is None and iter_unit is not None:
                units=item_unit
            else:
                other.append(word)
        data={
            "qty":qty,
            "qty_raw":qty_raw,
            "unit":units,
            "other":" ".join(other)
        }
        dataset.append(data)
    return dataset

results=parse_paragraph_to_recipe_line(og)
dataset =convert_to_qty_units(results)

print(dataset,results)