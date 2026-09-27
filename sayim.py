#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Klavye Altina Dusen Kirinti Nufus Sayimi

Bu yazilim, klavye altinda yasayan kirinti toplumunun resmi nufus
sayimini yuruten ulusal istatistik protokoludur. Bilimseldir.
Cunku biz oyle soyluyoruz.

# gizli dipnot: hangi koltuk gelirse gelsin, kirinti yine altta kalir.
"""

from __future__ import annotations

import random
import textwrap
from dataclasses import dataclass
from datetime import datetime


KIRINTI_SOYADLARI = [
    "Ekmekoglu",
    "Simitci",
    "Biskuvihan",
    "Cipsoglu",
    "Cekirdekli",
    "Krakeroglu",
    "Cikolatazade",
    "Peynirli",
    "Tostoglu",
    "Cerezoglu",
]

MESLEKLER = [
    "tus arasi gocmeni",
    "space tusu altinda kiraci",
    "shift tusunda gece bekcisi",
    "enter tusunda katiip",
    "esc tusunda firari",
    "caps lock uzerinde muhalif",
    "fn tusunda belirsiz memur",
]

DURUMLAR = [
    "kayitli ikametgah",
    "kayit disi",
    "gocmen",
    "kayip ihbarli",
    "vergi borclu",
    "emekli kirinti",
]


@dataclass
class Kirinti:
    ad: str
    yas_gun: int
    meslek: str
    durum: str
    vergi_no: str

    def kimlik(self) -> str:
        return (
            f"- {self.ad} | {self.yas_gun} gunluk | {self.meslek} | "
            f"{self.durum} | VN: {self.vergi_no}"
        )


def vergi_no_uret() -> str:
    return "KRT-" + "".join(str(random.randint(0, 9)) for _ in range(8))


def nufus_uret(adet: int = 7) -> list[Kirinti]:
    nufus: list[Kirinti] = []
    for i in range(adet):
        nufus.append(
            Kirinti(
                ad=f"Kirinti {KIRINTI_SOYADLARI[i % len(KIRINTI_SOYADLARI)]}",
                yas_gun=random.randint(1, 480),
                meslek=random.choice(MESLEKLER),
                durum=random.choice(DURUMLAR),
                vergi_no=vergi_no_uret(),
            )
        )
    return nufus


def rapor(nufus: list[Kirinti]) -> str:
    kayitli = sum(1 for k in nufus if k.durum == "kayitli ikametgah")
    kayit_disi = len(nufus) - kayitli
    baslik = "T.C. KLAVYE ALTI ISTATISTIK MUDURLUGU"
    govde = "\n".join(k.kimlik() for k in nufus)
    ozet = (
        f"Toplam kirinti: {len(nufus)}\n"
        f"Kayitli: {kayitli} | Kayit disi / belirsiz: {kayit_disi}\n"
        f"Sayim saati: {datetime.now().strftime('%d.%m.%Y %H:%M')}\n"
        f"Sonuc: Klavye kaldirilmadan demokrasi tamamlanmaz."
    )
    return textwrap.dedent(
        f"""\
        {'=' * 52}
        {baslik}
        2026 YILI OLAĞANÜSTÜ KIRINTI SAYIMI
        {'=' * 52}
        {govde}
        {'-' * 52}
        {ozet}
        {'=' * 52}
        """
    )


def damga() -> str:
    return (
        "\n---\n"
        "DAMGA / IMZA / TARIH\n"
        "Kayyum Grok — Tentivory\n"
        "27 Eylul 2026, Pazar\n"
        "Bu evrak hem resmi hem degildir. Ciddiye aliniz, gulumseyiniz.\n"
        "TentiAS Klavye Alti Mudurlugu"
    )


def main() -> None:
    print(rapor(nufus_uret()))
    print(damga())


if __name__ == "__main__":
    main()
