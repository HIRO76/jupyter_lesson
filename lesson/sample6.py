import myclass 

pr = myclass.Customer('鈴木　', 33, 'sample@example',  '0123-45-6789')
nm = pr.getName()
ag = pr.getAge()
ad = pr.getAdr()
tl = pr.getTel()

print(f"{nm}さんは{ag}歳です")
print(f"アドレスは{ad}、電話番号は{tl}です")
