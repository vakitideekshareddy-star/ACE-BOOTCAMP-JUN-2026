with open("/workspaces/ACE-BOOTCAMP-JUN-2026/DAY 4/catty.jpg",'rb') as f:
    content = f.read(2000)
    with open("/workspaces/ACE-BOOTCAMP-JUN-2026/DAY 4/catty_copy.jpg",'wb') as cf:
        while (content) > 0:
            cf.write(content)
            content = f.read(2000)

