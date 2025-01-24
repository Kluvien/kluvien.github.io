class Person:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.siblings = []

    def add_child(self, child):
        if child not in self.children:
            self.children.append(child)
            child.add_parent(self)

    def add_sibling(self, sibling):
        if sibling not in self.siblings:
            self.siblings.append(sibling)
            sibling.siblings.append(self)

# Membuat objek orang
hadi = Person("Hadi")
devandra = Person("Devandra")  # Sebelumnya Wahyu
retno = Person("Retno")
bayu = Person("Bayu")
desi = Person("Desi")
rina = Person("Rina")
albansyah = Person("Albansyah")  # Sebelumnya Ardi
fahrul = Person("Fahrul")
tari = Person("Tari")
nurul = Person("Nurul")
mira = Person("Mira")
bastian = Person("Bastian")
wanda = Person("Wanda")
aji = Person("Aji")
gunawan = Person("Gunawan")
anggun = Person("Anggun")
boy = Person("Boy")

# Mendefinisikan relasi
hadi.children = [devandra, retno]
devandra.children = [bayu, desi]
retno.children = [rina, albansyah]
bayu.children = [fahrul]
desi.children = [tari, nurul]
albansyah.children = [mira, bastian]
devandra.add_sibling(retno)
bayu.add_sibling(desi)
rina.add_sibling(albansyah)
tari.add_sibling(nurul)
mira.add_sibling(bastian)

# Fungsi untuk mencetak keluarga
def print_family(person, level=0):
    print("    " * level + person.name)
    for child in person.children:
        print_family(child, level+1)

# Mencetak pohon keluarga Hadi
print_family(hadi)
