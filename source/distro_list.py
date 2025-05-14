import json
from urllib.parse import urlparse

json_data = """
[
  {
    "distro": "Ubuntu",
    "website": "https://ubuntu.com/",
    "based": "Debian"
  },
  {
    "distro": "Linux Mint",
    "website": "https://linuxmint.com/",
    "based": "Ubuntu"
  },
  {
    "distro": "Debian",
    "website": "https://www.debian.org/",
    "based": "Independent"
  },
  {
    "distro": "Fedora",
    "website": "https://fedoraproject.org/",
    "based": "Independent (historically Red Hat Linux)"
  },
  {
    "distro": "Arch Linux",
    "website": "https://archlinux.org/",
    "based": "Independent"
  },
  {
    "distro": "Manjaro",
    "website": "https://manjaro.org/",
    "based": "Arch Linux"
  },
  {
    "distro": "openSUSE Leap",
    "website": "https://www.opensuse.org/",
    "based": "Independent (SUSE)"
  },
  {
    "distro": "openSUSE Tumbleweed",
    "website": "https://www.opensuse.org/",
    "based": "Independent (SUSE)"
  },
  {
    "distro": "CentOS Stream",
    "website": "https://www.centos.org/centos-stream/",
    "based": "Fedora (RHEL upstream)"
  },
  {
    "distro": "Rocky Linux",
    "website": "https://rockylinux.org/",
    "based": "RHEL"
  },
  {
    "distro": "AlmaLinux",
    "website": "https://almalinux.org/",
    "based": "RHEL"
  },
  {
    "distro": "Kali Linux",
    "website": "https://www.kali.org/",
    "based": "Debian"
  },
  {
    "distro": "Pop!_OS",
    "website": "https://pop.system76.com/",
    "based": "Ubuntu"
  },
  {
    "distro": "Zorin OS",
    "website": "https://zorinos.com/",
    "based": "Ubuntu"
  },
  {
    "distro": "MX Linux",
    "website": "https://mxlinux.org/",
    "based": "Debian"
  },
  {
    "distro": "Elementary OS",
    "website": "https://elementary.io/",
    "based": "Ubuntu"
  },
  {
    "distro": "Gentoo Linux",
    "website": "https://www.gentoo.org/",
    "based": "Independent"
  },
  {
    "distro": "Slackware",
    "website": "http://www.slackware.com/",
    "based": "Independent"
  },
  {
    "distro": "Kubuntu",
    "website": "https://kubuntu.org/",
    "based": "Ubuntu"
  },
  {
    "distro": "Lubuntu",
    "website": "https://lubuntu.me/",
    "based": "Ubuntu"
  },
  {
    "distro": "Xubuntu",
    "website": "https://xubuntu.org/",
    "based": "Ubuntu"
  },
  {
    "distro": "Ubuntu MATE",
    "website": "https://ubuntu-mate.org/",
    "based": "Ubuntu"
  },
  {
    "distro": "Ubuntu Budgie",
    "website": "https://ubuntubudgie.org/",
    "based": "Ubuntu"
  },
  {
    "distro": "KDE neon",
    "website": "https://neon.kde.org/",
    "based": "Ubuntu"
  },
  {
    "distro": "Solus",
    "website": "https://getsol.us/",
    "based": "Independent"
  },
  {
    "distro": "Void Linux",
    "website": "https://voidlinux.org/",
    "based": "Independent"
  },
  {
    "distro": "NixOS",
    "website": "https://nixos.org/",
    "based": "Independent"
  },
  {
    "distro": "Alpine Linux",
    "website": "https://alpinelinux.org/",
    "based": "Independent (musl, BusyBox)"
  },
  {
    "distro": "Puppy Linux",
    "website": "https://puppylinux.com/",
    "based": "Independent"
  },
  {
    "distro": "AntiX Linux",
    "website": "https://antixlinux.com/",
    "based": "Debian"
  },
  {
    "distro": "SparkyLinux",
    "website": "https://sparkylinux.org/",
    "based": "Debian"
  },
  {
    "distro": "Devuan",
    "website": "https://www.devuan.org/",
    "based": "Debian (systemd-free)"
  },
  {
    "distro": "Q4OS",
    "website": "https://q4os.org/",
    "based": "Debian"
  },
  {
    "distro": "Raspberry Pi OS",
    "website": "https://www.raspberrypi.com/software/",
    "based": "Debian"
  },
  {
    "distro": "EndeavourOS",
    "website": "https://endeavouros.com/",
    "based": "Arch Linux"
  },
  {
    "distro": "Garuda Linux",
    "website": "https://garudalinux.org/",
    "based": "Arch Linux"
  },
  {
    "distro": "Artix Linux",
    "website": "https://artixlinux.org/",
    "based": "Arch Linux (systemd-free)"
  },
  {
    "distro": "Clear Linux OS",
    "website": "https://clearlinux.org/",
    "based": "Independent (Intel)"
  },
  {
    "distro": "Oracle Linux",
    "website": "https://www.oracle.com/linux/",
    "based": "RHEL"
  },
  {
    "distro": "Mageia",
    "website": "https://www.mageia.org/",
    "based": "Mandriva (fork)"
  },
  {
    "distro": "PCLinuxOS",
    "website": "https://www.pclinuxos.com/",
    "based": "Mandriva (Mandrake)"
  },
  {
    "distro": "OpenMandriva Lx",
    "website": "https://www.openmandriva.org/",
    "based": "Mandriva (fork)"
  },
  {
    "distro": "ROSA Linux",
    "website": "https://www.rosalinux.ru/",
    "based": "Mandriva (fork)"
  },
  {
    "distro": "Red Hat Enterprise Linux (RHEL)",
    "website": "https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux",
    "based": "Independent (Fedora upstream)"
  },
  {
    "distro": "SUSE Linux Enterprise Server (SLES)",
    "website": "https://www.suse.com/products/server/",
    "based": "Independent (openSUSE is related)"
  },
  {
    "distro": "Deepin",
    "website": "https://www.deepin.org/",
    "based": "Debian"
  },
  {
    "distro": "Tails",
    "website": "https://tails.net/",
    "based": "Debian"
  },
  {
    "distro": "Qubes OS",
    "website": "https://www.qubes-os.org/",
    "based": "Fedora"
  },
  {
    "distro": "Whonix",
    "website": "https://www.whonix.org/",
    "based": "Debian"
  },
  {
    "distro": "Parrot OS",
    "website": "https://www.parrotsec.org/",
    "based": "Debian"
  },
  {
    "distro": "BlackArch Linux",
    "website": "https://blackarch.org/",
    "based": "Arch Linux"
  },
  {
    "distro": "Linux Lite",
    "website": "https://www.linuxliteos.com/",
    "based": "Ubuntu"
  },
  {
    "distro": "Peppermint OS",
    "website": "https://peppermintos.com/",
    "based": "Debian (previously Ubuntu)"
  },
  {
    "distro": "Bodhi Linux",
    "website": "https://www.bodhilinux.com/",
    "based": "Ubuntu"
  },
  {
    "distro": "Trisquel GNU/Linux",
    "website": "https://trisquel.info/",
    "based": "Ubuntu"
  },
  {
    "distro": "PureOS",
    "website": "https://pureos.net/",
    "based": "Debian"
  },
  {
    "distro": "Feren OS",
    "website": "https://ferenos.dev/",
    "based": "Ubuntu (Linux Mint)"
  },
  {
    "distro": "Nitrux",
    "website": "https://nxos.org/",
    "based": "Debian"
  },
  {
    "distro": "KaOS",
    "website": "https://kaosx.us/",
    "based": "Independent"
  },
  {
    "distro": "CRUX",
    "website": "https://crux.nu/",
    "based": "Independent"
  },
  {
    "distro": "Tiny Core Linux",
    "website": "http://tinycorelinux.net/",
    "based": "Independent (LFS)"
  },
  {
    "distro": "SliTaz GNU/Linux",
    "website": "https://www.slitaz.org/",
    "based": "Independent"
  },
  {
    "distro": "4MLinux",
    "website": "https://4mlinux.com/",
    "based": "Independent"
  },
  {
    "distro": "ArchLabs Linux",
    "website": "https://archlabslinux.com/",
    "based": "Arch Linux"
  },
  {
    "distro": "BunsenLabs Linux",
    "website": "https://www.bunsenlabs.org/",
    "based": "Debian"
  },
  {
    "distro": "LXLE",
    "website": "https://lxle.net/",
    "based": "Ubuntu (Lubuntu LTS)"
  },
  {
    "distro": "Salix OS",
    "website": "https://www.salixos.org/",
    "based": "Slackware"
  },
  {
    "distro": "VectorLinux",
    "website": "https://vectorlinux.com/",
    "based": "Slackware"
  },
  {
    "distro": "Absolute Linux",
    "website": "https://www.absolutelinux.org/",
    "based": "Slackware"
  },
  {
    "distro": "Porteus",
    "website": "http://www.porteus.org/",
    "based": "Slackware"
  },
  {
    "distro": "Slax",
    "website": "https://www.slax.org/",
    "based": "Debian (previously Slackware)"
  },
  {
    "distro": "Emmabuntüs",
    "website": "https://emmabuntus.org/",
    "based": "Debian (Ubuntu variants exist)"
  },
  {
    "distro": "GoboLinux",
    "website": "https://www.gobolinux.org/",
    "based": "Independent"
  },
  {
    "distro": "NuTyX",
    "website": "https://www.nutyx.org/",
    "based": "LFS (Linux From Scratch)"
  },
  {
    "distro": "Calculate Linux",
    "website": "https://www.calculate-linux.org/",
    "based": "Gentoo"
  },
  {
    "distro": "Pentoo",
    "website": "https://www.pentoo.ch/",
    "based": "Gentoo"
  },
  {
    "distro": "Redcore Linux",
    "website": "https://redcorelinux.org/",
    "based": "Gentoo"
  },
  {
    "distro": "Funtoo Linux",
    "website": "https://www.funtoo.org/",
    "based": "Gentoo (fork)"
  },
  {
    "distro": "Exherbo",
    "website": "https://www.exherbo.org/",
    "based": "Independent (source-based)"
  },
  {
    "distro": "T2 SDE",
    "website": "https://t2sde.org/",
    "based": "Independent (source-based kit)"
  },
  {
    "distro": "IPFire",
    "website": "https://www.ipfire.org/",
    "based": "LFS (Linux From Scratch)"
  },
  {
    "distro": "OpenMediaVault",
    "website": "https://www.openmediavault.org/",
    "based": "Debian"
  },
  {
    "distro": "Proxmox VE",
    "website": "https://www.proxmox.com/en/proxmox-virtual-environment",
    "based": "Debian"
  },
  {
    "distro": "TurnKey Linux Virtual Appliances",
    "website": "https://www.turnkeylinux.org/",
    "based": "Debian"
  },
  {
    "distro": "Univention Corporate Server (UCS)",
    "website": "https://www.univention.com/",
    "based": "Debian"
  },
  {
    "distro": "EasyOS",
    "website": "https://easyos.org/",
    "based": "Puppy Linux (Independent)"
  },
  {
    "distro": "Fatdog64",
    "website": "https://distro.ibiblio.org/fatdog/web/",
    "based": "Puppy Linux (Independent)"
  },
  {
    "distro": "SystemRescue",
    "website": "https://www.system-rescue.org/",
    "based": "Arch Linux"
  },
  {
    "distro": "Clonezilla Live",
    "website": "https://clonezilla.org/",
    "based": "Debian"
  },
  {
    "distro": "GParted Live",
    "website": "https://gparted.org/livecd.php",
    "based": "Debian"
  },
  {
    "distro": "Rescuezilla",
    "website": "https://rescuezilla.com/",
    "based": "Ubuntu"
  },
  {
    "distro": "ALT Linux",
    "website": "https://www.altlinux.org/",
    "based": "Independent (Mandriva lineage)"
  },
  {
    "distro": "Astra Linux",
    "website": "https://astralinux.ru/en/",
    "based": "Debian"
  },
  {
    "distro": "ClearOS",
    "website": "https://www.clearos.com/",
    "based": "RHEL/CentOS"
  },
  {
    "distro": "NethServer",
    "website": "https://www.nethserver.org/",
    "based": "RHEL/CentOS"
  },
  {
    "distro": "Endian Firewall Community",
    "website": "https://www.endian.com/community/efw-community/",
    "based": "RHEL"
  },
  {
    "distro": "Smoothwall Express",
    "website": "http://www.smoothwall.org/",
    "based": "Independent (LFS)"
  },
  {
    "distro": "LibreELEC",
    "website": "https://libreelec.tv/",
    "based": "Independent (JeOS for Kodi)"
  },
  {
    "distro": "OSMC (Open Source Media Center)",
    "website": "https://osmc.tv/",
    "based": "Debian"
  },
  {
    "distro": "Volumio",
    "website": "https://volumio.org/",
    "based": "Debian"
  },
  {
    "distro": "Lakka",
    "website": "https://www.lakka.tv/",
    "based": "LibreELEC (Independent)"
  },
  {
    "distro": "Recalbox",
    "website": "https://www.recalbox.com/",
    "based": "Independent (Buildroot)"
  },
  {
    "distro": "Batocera.linux",
    "website": "https://batocera.org/",
    "based": "Independent"
  },
  {
    "distro": "ChimeraOS",
    "website": "https://chimeraos.org/",
    "based": "Arch Linux"
  },
  {
    "distro": "Nobara Project",
    "website": "https://nobaraproject.org/",
    "based": "Fedora"
  },
  {
    "distro": "CachyOS",
    "website": "https://cachyos.org/",
    "based": "Arch Linux"
  },
  {
    "distro": "RebornOS",
    "website": "https://rebornos.org/",
    "based": "Arch Linux"
  },
  {
    "distro": "Archcraft",
    "website": "https://archcraft.io/",
    "based": "Arch Linux"
  },
  {
    "distro": "XeroLinux",
    "website": "https://xerolinux.xyz/",
    "based": "Arch Linux"
  },
  {
    "distro": "Bluestar Linux",
    "website": "https://bluestarlinux.org/",
    "based": "Arch Linux"
  },
  {
    "distro": "Hyperbola GNU/Linux-libre",
    "website": "https://www.hyperbola.info/",
    "based": "Arch Linux (moving to BSD kernel)"
  },
  {
    "distro": "Parabola GNU/Linux-libre",
    "website": "https://www.parabola.nu/",
    "based": "Arch Linux"
  },
  {
    "distro": "GeckoLinux",
    "website": "https://geckolinux.github.io/",
    "based": "openSUSE"
  },
  {
    "distro": "MakuluLinux",
    "website": "https://www.makululinux.com/",
    "based": "Debian"
  },
  {
    "distro": "Neptune",
    "website": "https://neptuneos.com/",
    "based": "Debian"
  },
  {
    "distro": "Siduction",
    "website": "https://siduction.org/",
    "based": "Debian (Unstable)"
  },
  {
    "distro": "AryaLinux",
    "website": "https://aryalinux.org/",
    "based": "LFS (Linux From Scratch)"
  },
  {
    "distro": "Venom Linux",
    "website": "https://venomlinux.org/",
    "based": "LFS (Linux From Scratch)"
  },
  {
    "distro": "Lunar Linux",
    "website": "https://www.lunar-linux.org/",
    "based": "Independent (source-based)"
  },
  {
    "distro": "Source Mage GNU/Linux",
    "website": "https://sourcemage.org/",
    "based": "Independent (source-based)"
  },
  {
    "distro": "Dragora GNU/Linux-Libre",
    "website": "https://dragora.org/",
    "based": "Independent"
  },
  {
    "distro": "Guix System",
    "website": "https://guix.gnu.org/",
    "based": "Independent (GNU)"
  },
  {
    "distro": "OpenWrt",
    "website": "https://openwrt.org/",
    "based": "Independent (for embedded devices)"
  },
  {
    "distro": "TrueNAS SCALE",
    "website": "https://www.truenas.com/truenas-scale/",
    "based": "Debian"
  },
  {
    "distro": "Photon OS",
    "website": "https://vmware.github.io/photon/",
    "based": "Independent (VMware)"
  },
  {
    "distro": "Amazon Linux 2",
    "website": "https://aws.amazon.com/amazon-linux-2/",
    "based": "RHEL/Fedora like"
  },
  {
    "distro": "Amazon Linux 2023",
    "website": "https://aws.amazon.com/linux/amazon-linux-2023/",
    "based": "Fedora"
  },
  {
    "distro": "Azure Linux (CBL-Mariner)",
    "website": "https://github.com/microsoft/CBL-Mariner",
    "based": "Independent (Microsoft)"
  },
  {
    "distro": "Endless OS",
    "website": "https://endlessos.com/",
    "based": "Debian"
  },
  {
    "distro": "Vanilla OS",
    "website": "https://vanillaos.org/",
    "based": "Debian (Immutable)"
  },
  {
    "distro": "blendOS",
    "website": "https://blendos.co/",
    "based": "Arch Linux (Immutable)"
  },
  {
    "distro": "Fedora Silverblue",
    "website": "https://silverblue.fedoraproject.org/",
    "based": "Fedora (Immutable)"
  },
  {
    "distro": "Fedora Kinoite",
    "website": "https://kinoite.fedoraproject.org/",
    "based": "Fedora (Immutable, KDE)"
  },
  {
    "distro": "openSUSE MicroOS",
    "website": "https://microos.opensuse.org/",
    "based": "openSUSE (Immutable)"
  },
  {
    "distro": "CarbonOS",
    "website": "https://carbon.sh/",
    "based": "Independent (Atomic, Flatpak-centric)"
  },
  {
    "distro": "Asahi Linux",
    "website": "https://asahilinux.org/",
    "based": "Arch Linux ARM (Fedora Asahi Remix exists)"
  },
  {
    "distro": "postmarketOS",
    "website": "https://postmarketos.org/",
    "based": "Alpine Linux"
  },
  {
    "distro": "Ubuntu Touch (UBports)",
    "website": "https://ubports.com/",
    "based": "Ubuntu"
  },
  {
    "distro": "Sailfish OS",
    "website": "https://sailfishos.org/",
    "based": "Mer (Linux, historically MeeGo)"
  },
  {
    "distro": "ChromeOS",
    "website": "https://www.google.com/chromebook/chrome-os/",
    "based": "Gentoo (Linux kernel)"
  },
  {
    "distro": "Fedora CoreOS",
    "website": "https://getfedora.org/coreos/",
    "based": "Fedora"
  },
  {
    "distro": "Flatcar Container Linux",
    "website": "https://www.flatcar.org/",
    "based": "CoreOS (fork)"
  },
  {
    "distro": "Talos Linux",
    "website": "https://www.talos.dev/",
    "based": "Independent (Minimalist, for Kubernetes)"
  },
  {
    "distro": "DietPi",
    "website": "https://dietpi.com/",
    "based": "Debian"
  },
  {
    "distro": "Armbian",
    "website": "https://www.armbian.com/",
    "based": "Debian/Ubuntu (for ARM boards)"
  },
  {
    "distro": "Manjaro ARM",
    "website": "https://manjaro.org/download/#ARM",
    "based": "Arch Linux ARM"
  },
  {
    "distro": "Arch Linux ARM",
    "website": "https://archlinuxarm.org/",
    "based": "Arch Linux"
  },
  {
    "distro": "Adelie Linux",
    "website": "https://adelielinux.org/",
    "based": "Independent (musl, for various architectures)"
  },
  {
    "distro": "Bedrock Linux",
    "website": "https://bedrocklinux.org/",
    "based": "Meta-distribution (allows mixing components)"
  },
  {
    "distro": "Cucumber Linux",
    "website": "https://cucumberlinux.com/",
    "based": "LFS (Linux From Scratch)"
  },
  {
    "distro": "Void PPC",
    "website": "https://voidlinux-ppc.org/",
    "based": "Void Linux (for PowerPC)"
  },
  {
    "distro": "Plop Linux",
    "website": "https://www.plop.at/en/ploplinux/index.html",
    "based": "Independent (LFS)"
  },
  {
    "distro": "paldo GNU/Linux",
    "website": "https://www.paldo.org/",
    "based": "Independent (source and binary)"
  },
  {
    "distro": "Pisi Linux",
    "website": "https://pisilinux.org/",
    "based": "Pardus (Independent package manager)"
  },
  {
    "distro": "Tizen",
    "website": "https://www.tizen.org/",
    "based": "Linux kernel (Samsung, Linux Foundation)"
  },
  {
    "distro": "webOS Open Source Edition",
    "website": "https://www.webosose.org/",
    "based": "Linux kernel (LG)"
  },
  {
    "distro": "KaiOS",
    "website": "https://www.kaiostech.com/",
    "based": "Firefox OS (Linux kernel)"
  },
  {
    "distro": "Elive",
    "website": "https://www.elivecd.org/",
    "based": "Debian"
  },
  {
    "distro": "Vine Linux",
    "website": "http://vinelinux.org/ (Largely historical)",
    "based": "Fedora"
  },
  {
    "distro": "Sabayon Linux",
    "website": "https://www.sabayon.org/ (Discontinued)",
    "based": "Gentoo"
  },
  {
    "distro": "Scientific Linux",
    "website": "https://www.scientificlinux.org/ (EOL)",
    "based": "RHEL"
  },
  {
    "distro": "CentOS (pre-Stream)",
    "website": "https://www.centos.org/ (EOL)",
    "based": "RHEL"
  },
  {
    "distro": "SteamOS",
    "website": "https://store.steampowered.com/steamos/",
    "based": "Debian (v3 Arch Linux)"
  },
  {
    "distro": "HoloISO",
    "website": "https://github.com/theVakhovskeIsTaken/holoiso",
    "based": "Arch Linux"
  },
  {
    "distro": "Drauger OS",
    "website": "https://draugeros.org/",
    "based": "Ubuntu"
  },
  {
    "distro": "wattOS",
    "website": "https://www.planetwatt.com/",
    "based": "Debian"
  },
  {
    "distro": "Damn Small Linux",
    "website": "http://www.damnsmalllinux.org/ (Historical)",
    "based": "Knoppix (Debian)"
  },
  {
    "distro": "Finnix",
    "website": "https://www.finnix.org/",
    "based": "Debian"
  },
  {
    "distro": "Grml",
    "website": "https://grml.org/",
    "based": "Debian"
  },
  {
    "distro": "Porteus Kiosk",
    "website": "https://porteus-kiosk.org/",
    "based": "Gentoo"
  },
  {
    "distro": "Thinstation",
    "website": "https://thinstation.org/",
    "based": "LFS (Linux From Scratch)"
  },
  {
    "distro": "VyOS",
    "website": "https://vyos.io/",
    "based": "Debian"
  },
  {
    "distro": "Untangle NG Firewall",
    "website": "https://www.untangle.com/",
    "based": "Debian"
  },
  {
    "distro": "Security Onion",
    "website": "https://securityonionsolutions.com/",
    "based": "Ubuntu"
  },
  {
    "distro": "Proxmox Backup Server",
    "website": "https://www.proxmox.com/en/proxmox-backup-server",
    "based": "Debian"
  },
  {
    "distro": "Obarun",
    "website": "https://obarun.org/",
    "based": "Arch Linux"
  },
  {
    "distro": "Slackel",
    "website": "https://www.slackel.gr/",
    "based": "Slackware"
  },
  {
    "distro": "Slint",
    "website": "https://slint.fr/",
    "based": "Slackware"
  },
  {
    "distro": "Zentyal Server",
    "website": "https://zentyal.com/",
    "based": "Ubuntu"
  },
  {
    "distro": "SME Server",
    "website": "https://wiki.koozali.org/",
    "based": "RHEL/CentOS"
  },
  {
    "distro": "Rockstor",
    "website": "https://rockstor.com/",
    "based": "openSUSE"
  },
  {
    "distro": "EasyNAS",
    "website": "https://easynas.org/",
    "based": "openSUSE"
  },
  {
    "distro": "Ufficio Zero",
    "website": "https://www.ufficiozero.org/",
    "based": "PCLinuxOS"
  },
  {
    "distro": "BOSS Linux",
    "website": "https://bosslinux.in/",
    "based": "Debian"
  },
  {
    "distro": "Nova Linux",
    "website": "https://www.nova.cu/",
    "based": "Ubuntu"
  },
  {
    "distro": "Canaima GNU/Linux",
    "website": "https://canaima.softwarelibre.gob.ve/",
    "based": "Debian"
  },
  {
    "distro": "ArchBang",
    "website": "https://archbang.org/",
    "based": "Arch Linux"
  },
  {
    "distro": "ArchStrike",
    "website": "https://archstrike.org/",
    "based": "Arch Linux"
  },
  {
    "distro": "Archman",
    "website": "https://archman.org/",
    "based": "Arch Linux"
  },
  {
    "distro": "Antergos",
    "website": "https://antergos.com/ (Discontinued)",
    "based": "Arch Linux"
  },
  {
    "distro": "SolydXK",
    "website": "https://solydxk.com/",
    "based": "Debian"
  },
  {
    "distro": "Refracta",
    "website": "https://www.refracta.org/",
    "based": "Devuan"
  },
  {
    "distro": "KNOPPIX",
    "website": "https://www.knopper.net/knoppix/index-en.html",
    "based": "Debian"
  },
  {
    "distro": "Asianux",
    "website": "http://www.asianux.com/ (Largely historical/merged)",
    "based": "RHEL"
  },
  {
    "distro": "Berry Linux",
    "website": "http://berry-lab.net/",
    "based": "Fedora"
  },
  {
    "distro": "BLAG Linux and GNU",
    "website": "https://blag.fsf.org/ (Inactive)",
    "based": "Fedora"
  },
  {
    "distro": "EnGarde Secure Linux",
    "website": "https://www.engardelinux.org/ (Likely inactive)",
    "based": "Fedora"
  },
  {
    "distro": "Hanthana Linux",
    "website": "https://hanthana.org/ (Status unclear)",
    "based": "Fedora"
  },
  {
    "distro": "Korora",
    "website": "https://kororaproject.org/ (Discontinued)",
    "based": "Fedora"
  },
  {
    "distro": "Linpus Linux",
    "website": "https://www.linpus.com/",
    "based": "Fedora"
  }
]
"""

# Load the JSON data
distro_list = json.loads(json_data)

# Print the information for each distribution in the new format
for item in distro_list:
    distro_name = item['distro']
    website_url = item['website']
    base_distro = item['based']

    # Parse website to get the domain
    parsed_url = urlparse(website_url)
    domain = parsed_url.netloc
    if not domain: # Handle cases where netloc might be empty for malformed URLs or local file paths
        domain = website_url # Fallback to the original string if parsing fails to produce a netloc
    else:
        # Optional: remove 'www.' if present for a cleaner look, as in the example "ubuntu.com"
        if domain.startswith('www.'):
            domain = domain[4:]
    
    # Handle cases where the website might be a GitHub link or similar and we want a cleaner representation
    # For example, if website is "https://github.com/microsoft/CBL-Mariner", domain becomes "github.com"
    # If the original URL itself is simple like "https://distro.ibiblio.org/fatdog/web/", netloc is "distro.ibiblio.org"
    # The example "ubuntu.com" implies just the core domain.
    # If the URL doesn't have a scheme (e.g., "vinelinux.org/ (Largely historical)"), urlparse might behave differently.
    # Let's assume URLs are generally well-formed with schemes.
    # For a simple domain like "github.com/user/repo", if you only want "github.com", netloc is fine.

    print(f"Distro's name: {distro_name}, Website: {domain}, Based: {base_distro}")

print(f"\nTotal Linux distributions listed: {len(distro_list)}")