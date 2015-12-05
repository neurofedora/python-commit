%global modname commit

%global commit 20b742d2d6a9b530a3fb3436b637442026776b00
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-%{modname}
Version:        1.0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Convex Optimization Modeling for Microstructure Informed Tractography

License:        GPLv3+
URL:            https://github.com/daducci/COMMIT
Source0:        https://github.com/daducci/COMMIT/archive/%{commit}/%{modname}-%{shortcommit}.tar.gz

%description
The reconstructions recovered with existing tractography algorithms are not
really quantitative even though diffusion MRI is a quantitative modality by
nature. As a matter of fact, several techniques have been proposed in recent
years to estimate, at the voxel level, intrinsic micro-structural features of
the tissue, such as axonal density and diameter, by using multi-compartment
models. COMMIT implements a novel framework to re-establish the link between
tractography and tissue micro-structure.

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel Cython
%if 0%{?fedora} > 23
BuildRequires:  python2-numpy
Requires:       python2-numpy%{?isa}
%else
BuildRequires:  numpy
Requires:       numpy%{?isa}
%endif
Requires:       python2-nibabel
Requires:       python2-amico

%description -n python2-%{modname}
The reconstructions recovered with existing tractography algorithms are not
really quantitative even though diffusion MRI is a quantitative modality by
nature. As a matter of fact, several techniques have been proposed in recent
years to estimate, at the voxel level, intrinsic micro-structural features of
the tissue, such as axonal density and diameter, by using multi-compartment
models. COMMIT implements a novel framework to re-establish the link between
tractography and tissue micro-structure.

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  /usr/bin/2to3
BuildRequires:  python3-devel python3-Cython
BuildRequires:  python3-numpy
Requires:       python3-numpy%{?isa}
Requires:       python3-nibabel
Requires:       python3-amico

%description -n python3-%{modname}
The reconstructions recovered with existing tractography algorithms are not
really quantitative even though diffusion MRI is a quantitative modality by
nature. As a matter of fact, several techniques have been proposed in recent
years to estimate, at the voxel level, intrinsic micro-structural features of
the tissue, such as axonal density and diameter, by using multi-compartment
models. COMMIT implements a novel framework to re-establish the link between
tractography and tissue micro-structure.

Python 3 version.

%prep
%setup -qc
mv COMMIT-%{commit} python2

cp -a python2 python3
2to3 --write --nobackups python3

%build
pushd python2
  %py2_build
popd

pushd python3
  %py3_build
popd

%install
pushd python2
  %py2_install
popd

pushd python3
  %py3_install
popd

%files -n python2-%{modname}
%license python2/LICENSE
%doc python2/README.md
%{python2_sitearch}/%{modname}*

%files -n python3-%{modname}
%license python3/LICENSE
%doc python3/README.md
%{python3_sitearch}/%{modname}*

%changelog
* Sat Dec 05 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0-0.1.git20b742d
- Initial package
