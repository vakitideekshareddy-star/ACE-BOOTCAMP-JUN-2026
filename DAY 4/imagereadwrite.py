with open("/workspaces/ACE-BOOTCAMP-JUN-2026/DAY 4/catty.jpg",'rb') as f:
    content = f.read()
    with open("/workspaces/ACE-BOOTCAMP-JUN-2026/DAY 4/catty_copy.jpg",'wb') as cf:
        cf.write(content)