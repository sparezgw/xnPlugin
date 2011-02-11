from xml.etree.ElementTree import ElementTree


if __name__ == '__main__':
    tree = ElementTree()
    tree.parse("pets.xml")
    dataroot = tree.find('Data')
    print dataroot.get('UserId')
