from hero import Hero
from monster import Monster

if __name__ == "__main__":
    print("=== SELAMAT DATANG DI ARENA RPG OOP ===")
    
    # Instansiasi Object
    nama_hero = input("jayen: ") or "Gatotkaca"
    pahlawan = Hero(nama=nama_hero, hp=100, attack_power=15, class_hero="Tanker")
    musuh = Monster(nama="Goblin Jahat", hp=90, attack_power=10, jenis="Humanoid")

    print(f"\n🎮 Pertandingan Dimulai: {pahlawan.nama} vs {musuh.nama}!\n")
    print("-" * 40)

    ronde = 1
    while pahlawan.hp > 0 and musuh.hp > 0:
        print(f"\n[ Ronde {ronde} ]")
        print(pahlawan.status())
        print(musuh.status())
        print("-" * 25)
        print("Pilih Aksi Kamu:")
        print("1. Serangan Biasa")
        print("2. Skill Khusus (Ultimate)")
        
        pilihan = input("Masukkan pilihan (1/2): ")
        print()

        # Giliran Hero menyerang berdasarkan input user
        if pilihan == "2":
            pahlawan.skill_khusus(musuh)
        else:
            pahlawan.serang(musuh)

        # Cek apakah monster sudah kalah
        if musuh.hp <= 0:
            break

        print()
        # Giliran Monster menyerang balik secara otomatis
        musuh.serang(pahlawan)

        ronde += 1
        print("=" * 40)

    print("\n" + "=" * 40)
    if pahlawan.hp > 0:
        print(f"🎉 SELAMAT! {pahlawan.nama} berhasil mengalahkan {musuh.nama} dan keluar sebagai PEMENANG!")
    else:
        print(f"💀 GAME OVER! {pahlawan.nama} telah dikalahkan oleh {musuh.nama}...")
    print("=" * 40)