Name:           pushover
Version:        0.0.5
Release:        10%{?dist}
Summary:        Fun puzzle game with dominos

# Some proprietary graphics from the original game are still used
License:        GPLv3 and proprietary
URL:            https://pushover.github.io/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.appdata.xml

BuildRequires:  gcc-c++
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_ttf-devel
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel
BuildRequires:  lua-devel
BuildRequires:  gettext
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Requires:       hicolor-icon-theme
Requires:       gnu-free-sans-fonts


%description
Rearrange the dominoes on the different platforms so that you can start a 
chain reaction that makes all dominoes topple over.


%prep
%setup -q

# Fix char encoding
iconv --from=ISO-8859-1 --to=UTF-8 ChangeLog > ChangeLog.utf8
touch -r ChangeLog ChangeLog.utf8
mv ChangeLog.utf8 ChangeLog


%build
%configure
%make_build


%install
%make_install

# Symlink system font
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/data/FreeSans.ttf
ln -s %{_datadir}/fonts/gnu-free/FreeSans.ttf \
    $RPM_BUILD_ROOT%{_datadir}/%{name}/data/FreeSans.ttf

# Install icons (16, 32, 48, 64px)
for i in 0 1 2 3; do
  px=$(expr ${i} \* 16 + 16)
  install -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${px}x${px}/apps
  convert %{name}.ico[${i}] \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${px}x${px}/apps/%{name}.png
done

# Install desktop file
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}

# Install AppData file
install -d $RPM_BUILD_ROOT%{_datadir}/metainfo
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/metainfo
appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%{_datadir}/metainfo/*.appdata.xml


%find_lang %{name}


%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/metainfo/%{name}.appdata.xml
%doc %{_pkgdocdir}
%exclude %{_pkgdocdir}/COPYING
%license COPYING


%changelog
* Sat Mar 17 2018 Andrea Musuruane <musuruan@gmail.com> - 0.0.5-10
- Updated URL
- Added gcc-c++ dependency
- Removed obsolete scriptlets
- Added license tag
- Added AppData file
- Spec file clean up

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 26 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 01 2014 Sérgio Basto <sergio@serjux.com> - 0.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Dec 31 2013 Andrea Musuruane <musuruan@gmail.com> 0.0.5-5
- Pushover already supports lua-5.2

* Tue Dec 31 2013 Andrea Musuruane <musuruan@gmail.com> 0.0.5-4
- Dropped cleaning at the beginning of %%install

* Tue Dec 31 2013 Andrea Musuruane <musuruan@gmail.com> 0.0.5-3
- Built with compat-lua for F20+

* Mon Aug 12 2013 Andrea Musuruane <musuruan@gmail.com> 0.0.5-2
- Dropped obsolete Group, Buildroot, %%clean and %%defattr

* Mon May 20 2013 Andrea Musuruane <musuruan@gmail.com> 0.0.5-1
- New upstream release

* Sun Jan 27 2013 Andrea Musuruane <musuruan@gmail.com> 0.0.4-1
- New upstream release

* Thu Mar 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.0.3-4
- Rebuilt for c++ ABI breakage

* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jun 05 2011 Andrea Musuruane <musuruan@gmail.com> 0.0.3-2
- Rebuilt

* Mon May 30 2011 Andrea Musuruane <musuruan@gmail.com> 0.0.3-1
- New upstream release
- Packaged new desktop icons

* Tue Jan 05 2010 Andrea Musuruane <musuruan@gmail.com> 0.0.2-2
- Fixed license
- Fixed typo
- More consistent macro usage
- Cosmetic changes

* Sat Dec 26 2009 Andrea Musuruane <musuruan@gmail.com> 0.0.2-1
- First release

