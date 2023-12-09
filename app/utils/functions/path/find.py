from glob import glob



def find_pfx():
    results = glob("*.pfx")
    if len(results)>0:return results[0]
    return ""