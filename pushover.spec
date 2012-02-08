Name:           pushover
Version:        0.0.3
Release:        3%{?dist}
Summary:        Fun puzzle game with dominos

Group:          Amusements/Games
# Some proprietary graphics from the original game are still used
License:        GPLv3 and proprietary
URL:            http://pushover.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_ttf-devel
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel
BuildRequires:  lua-devel
BuildRequires:  gettext
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme
Requires:       gnu-free-sans-fonts


%description
Rearrange the dominoes on the different platforms so that you can start a 
chainreaction that makes all dominoes topple over.


%prep
%setup -q

# Fix char encoding
iconv --from=ISO-8859-1 --to=UTF-8 ChangeLog > ChangeLog.utf8
touch -r ChangeLog ChangeLog.utf8
mv ChangeLog.utf8 ChangeLog


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# Remove installed docs
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}/

# Symlink system font
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/data/FreeSans.ttf
ln -s %{_datadir}/fonts/gnu-free/FreeSans.ttf \
    $RPM_BUILD_ROOT%{_datadir}/%{name}/data/FreeSans.ttf

# Install icons (16, 32, 48, 64px)
for i in 0 1 2 3; do
  px=$(expr ${i} \* 16 + 16)
  mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${px}x${px}/apps
  convert %{name}.ico[${i}] \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${px}x${px}/apps/%{name}.png
done

# Install desktop file
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}

%find_lang %{name}


%clean
rm -rf $RPM_BUILD_ROOT


%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi


%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files -f %{name}.lang
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%doc AUTHORS ChangeLog COPYING NEWS readme.txt


%changelog
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

