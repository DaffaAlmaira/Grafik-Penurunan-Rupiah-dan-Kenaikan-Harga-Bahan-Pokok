import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.widgets import Button

data= {
    'periode' : ['20 Mei 2024' , '4 Juni 2024' , '20 Mei 2026' , '4 Juni 2026'],
    'Kurs_Jual_Per_1_Dolar_Berdasarkan_Data_BI' : [16057.89, 16306.13, 17807.60, 18020.65]
}

df = pd.DataFrame(data)
sns.set_theme(style="whitegrid")

def halaman_1(event=None):
        global btn_next
        global ax_back
        if 'ax_back' in globals() and ax_back is not None:
            ax_back.remove()
            ax_back = None
        plt.clf()
        plt.plot(df['periode'], df['Kurs_Jual_Per_1_Dolar_Berdasarkan_Data_BI'], marker='o')
        plt.title("Perubahan Kurs Jual Dari Tahun 2024 Menuju 2026 Berdasarkan Data BI", pad=15)
        plt.xlabel("Periode")
        plt.ylabel("Kurs Jual Rupiah Per 1 Dolar", labelpad=15)
        plt.ylim(16000, 18500)

        for i in range(4) :
            x = df['periode'][i]
            y = df['Kurs_Jual_Per_1_Dolar_Berdasarkan_Data_BI'][i]
            plt.annotate(f"{y}", (x, y), textcoords="offset points", xytext=(0, 10), ha='center')

        ax_next = plt.axes([0.88, 0.4, 0.1, 0.075])
        btn_next = Button(ax_next, "Next", color='tomato', hovercolor='crimson')
        btn_next.on_clicked(pindah_halaman)
        plt.subplots_adjust(right=0.85)
        plt.draw()


def pindah_halaman(event=None):
        plt.clf()
        periode_baru = ['20 Mei 2024' , '4 Juni 2024' , '20 Mei 2026' , '4 Juni 2026']
        Kurs_Beli_Per_1_Dolar_Berdasarkan_Data_BI = [15898.11, 16143.88, 17630.40, 17841.35]
        plt.plot(periode_baru, Kurs_Beli_Per_1_Dolar_Berdasarkan_Data_BI, marker='o', color='crimson')
        plt.title("Perubahan Kurs Beli Dari Tahun 2024 Menuju 2026 Berdasarkan Data BI", pad=15)
        plt.xlabel("Periode")
        plt.ylabel("Kurs Beli Rupiah Per 1 Dolar", labelpad=15)
        plt.ylim(15500, 18000)
        plt.grid(True)

        for i in range(4) :
            x = periode_baru[i]
            y = Kurs_Beli_Per_1_Dolar_Berdasarkan_Data_BI[i]
            plt.annotate(f"{y}", (x, y), textcoords="offset points", xytext=(0, 10), ha='center')

        ax_next2 = plt.axes([0.88, 0.4, 0.1, 0.075])
        global btn_next
        btn_next = Button(ax_next2, "Next", color='tomato', hovercolor='crimson')
        global ax_back
        ax_back = plt.axes([0.01, 0.4, 0.1, 0.075])
        if 'ax_back2' in globals() and ax_back is not None:
              ax_back.remove()
              ax_back = None
        global btn_back
        btn_back = Button(ax_back, "Back", color='tomato', hovercolor='crimson')
        plt.subplots_adjust(left=0.19, right=0.86)
        plt.draw()
        btn_back.on_clicked(halaman_1)
        btn_next.on_clicked(pindah_halaman2)
halaman_1()


def pindah_halaman2(event=None):
        plt.clf()
        periode_baru = ['20 Mei 2024' , '4 Juni 2024' , '20 Mei 2026' , '4 Juni 2026']
        harga_bahan_pokok = [13600, 13553, 13757, 13776]
        plt.plot(periode_baru, harga_bahan_pokok, marker='o', color='tomato')
        plt.title("Perubahan Harga Bahan Pokok Beras (kg) Berdasarkan Data dari SP2KP - Kementerian Perdagangan", pad=15)
        plt.xlabel("Periode")
        plt.ylabel("Harga Bahan Dalam Rupiah", labelpad=15)
        plt.ylim(13000, 14000)
        plt.grid(True)

        for i in range(4) :
            x = periode_baru[i]
            y = harga_bahan_pokok[i]
            plt.annotate(f"{y}", (x, y), textcoords="offset points", xytext=(0, 10), ha='center')

        global btn_next
        ax_next3 = plt.axes([0.88, 0.4, 0.1, 0.075])
        btn_next = Button(ax_next3, "Next", color='tomato', hovercolor='crimson')
        global ax_back
        ax_back = plt.axes([0.01, 0.4, 0.1, 0.075])
        if 'ax_back2' in globals() and ax_back is not None:
              ax_back.remove()
              ax_back = None
        global btn_back
        btn_back = Button(ax_back, "Back", color='tomato', hovercolor='crimson')
        plt.subplots_adjust(left=0.19, right=0.86)
        plt.draw()
        btn_back.on_clicked(pindah_halaman)
        btn_next.on_clicked(pindah_halaman3)


def pindah_halaman3(eevent=None):
      plt.clf()
      periode_baru = ['20 Mei 2024' , '4 Juni 2024' , '20 Mei 2026' , '4 Juni 2026']
      harga_bahan_pokok = [17819, 17725, 18278, 18257]
      plt.plot(periode_baru, harga_bahan_pokok, marker='o', color='tomato')
      plt.title("Perubahan Harga Bahan Pokok Gula Pasir Curah (kg) Berdasarkan Data dari SP2KP - Kementerian Perdagangan", pad=15)
      plt.xlabel("Periode")
      plt.ylabel("Harga Bahan Dalam Rupiah", labelpad=15)
      plt.ylim(17000, 18500)
      plt.grid(True)

      for i in range(4) :
            x = periode_baru[i]
            y = harga_bahan_pokok[i]
            plt.annotate(f"{y}", (x, y), textcoords="offset points", xytext=(0, 10), ha='center')

      global btn_next
      ax_next4 = plt.axes([0.88, 0.4, 0.1, 0.075])
      btn_next = Button(ax_next4, "Next", color='tomato', hovercolor='crimson')
      global ax_back
      ax_back = plt.axes([0.01, 0.4, 0.1, 0.075])
      if 'ax_back2' in globals() and ax_back is not None:
              ax_back.remove()
              ax_back = None
      global btn_back
      btn_back = Button(ax_back, "Back", color='tomato', hovercolor='crimson')
      plt.subplots_adjust(left=0.19, right=0.86)
      plt.draw()
      btn_back.on_clicked(pindah_halaman2)
      btn_next.on_clicked(pindah_halaman4)


def pindah_halaman4 (event=None):
      plt.clf()
      periode_baru = ['20 Mei 2024' , '4 Juni 2024' , '20 Mei 2026' , '4 Juni 2026']
      harga_bahan_pokok = [40644, 41348, 66228, 68904]
      plt.plot(periode_baru, harga_bahan_pokok, marker='o', color='tomato')
      plt.title("Perubahan Harga Bahan Pokok Cabai Rawit Merah (kg) Berdasarkan Data dari SP2KP - Kementerian Perdagangan", pad=15)
      plt.xlabel("Periode")
      plt.ylabel("Harga Bahan Dalam Rupiah", labelpad=15)
      plt.ylim(40000, 70000)
      plt.grid(True)

      for i in range(4) :
            x = periode_baru[i]
            y = harga_bahan_pokok[i]
            plt.annotate(f"{y}", (x, y), textcoords="offset points", xytext=(0, 10), ha='center')

      global btn_next
      ax_next4 = plt.axes([0.88, 0.4, 0.1, 0.075])
      btn_next = Button(ax_next4, "Next", color='tomato', hovercolor='crimson')
      global ax_back
      ax_back = plt.axes([0.01, 0.4, 0.1, 0.075])
      if 'ax_back2' in globals() and ax_back is not None:
              ax_back.remove()
              ax_back = None
      global btn_back
      btn_back = Button(ax_back, "Back", color='tomato', hovercolor='crimson')
      plt.subplots_adjust(left=0.19, right=0.86)
      plt.draw()
      btn_back.on_clicked(pindah_halaman3)
      btn_next.on_clicked(pindah_halaman5)


def pindah_halaman5 (event=None):
      plt.clf()
      periode_baru = ['20 Mei 2024' , '4 Juni 2024' , '20 Mei 2026' , '4 Juni 2026']
      harga_bahan_pokok = [132780, 132799, 139732, 141084]
      plt.plot(periode_baru, harga_bahan_pokok, marker='o', color='tomato')
      plt.title("Perubahan Harga Bahan Pokok Daging Sapi Paha Belakang (kg) Berdasarkan Data dari SP2KP - Kementerian Perdagangan", pad=15)
      plt.xlabel("Periode")
      plt.ylabel("Harga bahan Dalam Rupiah", labelpad=15)
      plt.ylim(132000, 142000)
      plt.grid(True)

      for i in range(4) :
            x = periode_baru[i]
            y = harga_bahan_pokok[i]
            plt.annotate(f"{y}", (x, y), textcoords="offset points", xytext=(0, 10), ha='center')

      global btn_next
      ax_next4 = plt.axes([0.88, 0.4, 0.1, 0.075])
      btn_next = Button(ax_next4, "Next", color='tomato', hovercolor='crimson')
      global ax_back
      ax_back = plt.axes([0.01, 0.4, 0.1, 0.075])
      if 'ax_back2' in globals() and ax_back is not None:
              ax_back.remove()
              ax_back = None
      global btn_back
      btn_back = Button(ax_back, "Back", color='tomato', hovercolor='crimson')
      plt.subplots_adjust(left=0.19, right=0.86)
      plt.draw()
      btn_back.on_clicked(pindah_halaman4)
      btn_next.on_clicked(pindah_halaman6)


def pindah_halaman6 (event=None):
      plt.clf()
      periode_baru = ['20 Mei 2024' , '4 Juni 2024' , '20 Mei 2026' , '4 Juni 2026']
      harga_bahan_pokok = [15531, 15576, 19609, 19633]
      plt.plot(periode_baru, harga_bahan_pokok, marker='o', color='tomato')
      plt.title("Perubahan Harga Bahan Pokok Minyak Goreng Sawit Curah (lt) Berdasarkan Data dari SP2KP - Kementerian Perdagangan", pad=15)
      plt.xlabel("Periode")
      plt.ylabel("Harga bahan Dalam Rupiah", labelpad=15)
      plt.ylim(15000, 20000)
      plt.grid(True)

      for i in range(4) :
            x = periode_baru[i]
            y = harga_bahan_pokok[i]
            plt.annotate(f"{y}", (x, y), textcoords="offset points", xytext=(0, 10), ha='center')

      global btn_next
      ax_next4 = plt.axes([0.88, 0.4, 0.1, 0.075])
      btn_next = Button(ax_next4, "Next", color='tomato', hovercolor='crimson')
      ax_next4.remove()
      global ax_back
      ax_back = plt.axes([0.01, 0.4, 0.1, 0.075])
      if 'ax_back2' in globals() and ax_back is not None:
              ax_back.remove()
              ax_back = None
      global btn_back
      btn_back = Button(ax_back, "Back", color='tomato', hovercolor='crimson')
      plt.subplots_adjust(left=0.19, right=0.86)
      plt.draw()
      btn_back.on_clicked(pindah_halaman5)

plt.show()