## [3.1.1](https://github.com/jrappen/sublime-auto-dark/compare/3.1.0...3.1.1) (2020-05-03)


### Bug Fixes

* **PkgCtrl:** Bump requirements ([ad6e079](https://github.com/jrappen/sublime-auto-dark/commit/ad6e07973a976d725172f271d41a0a615e7d6708))



# [3.1.0](https://github.com/jrappen/sublime-auto-dark/compare/3.0.0...3.1.0) (2020-05-03)

### Features

* **GitHub:** Use default community health files ([f1614c7](https://github.com/jrappen/sublime-auto-dark/commit/f1614c720048099ed31b371693815186bad03796))

### Bug Fixes

* **mdpopups:** Remove passing `cmd` to `mdpopups` ([d41d5b3](https://github.com/jrappen/sublime-auto-dark/commit/d41d5b375b2794c7cd894c36c38c878db6735883))
* **Preferences:** Add default pref location info ([93b389b](https://github.com/jrappen/sublime-auto-dark/commit/93b389b7068c99ab7778017764b889ddc3809443))
* **PkgCtrl:** Update installation instructions ([d988a7a](https://github.com/jrappen/sublime-auto-dark/commit/d988a7a0b46e981dc13450e661a3933d1aa772a6))

# 3.0.0 (2020-03-25)

### BREAKING CHANGES

* **Python:** Also toggle sublime theme

### Features

* **Python:** Also toggle sublime theme ([65e1459](https://github.com/jrappen/sublime-auto-dark/commit/65e145908ba45b756eca4039bbf7eee45e75a5a9))

### Bug Fixes

* **docs:** Update docs for v3.0.0 ([eed3b91](https://github.com/jrappen/sublime-auto-dark/commit/eed3b91cd4c93b6558f4b27091a18cbff7fe5378))
* **GitHub:** Update issue templates ([21a1b0f](https://github.com/jrappen/sublime-auto-dark/commit/21a1b0f7898b78c1b14358ed0709ee5636dacecd))
* **PkgCtrl:** Fix supported version range for ST3 ([d6bade3](https://github.com/jrappen/sublime-auto-dark/commit/d6bade313484733c693636715fdaa9082e2b9b68))
* **PkgCtrl:** Use `"tags": true` for ST4 tags ([b02afb1](https://github.com/jrappen/sublime-auto-dark/commit/b02afb148e3128d7f2d09ea382e296c8ed967819))
* **Sublime Text:** Supported version range for ST3 ([bcfc128](https://github.com/jrappen/sublime-auto-dark/commit/bcfc12876e809a856ba83afc510895e3faf6f46e))

# 2.0.0 (2020-03-16)

### BREAKING CHANGES

* **Sublime Text:** Add ST3 support

### Features

* **Sublime Text:** Add ST3 support ([9009d30](https://github.com/jrappen/sublime-auto-dark/commit/9009d30cdd4d74f1882bb4a0cb697d416d993474)), closes [jrappen/sublime-auto-dark#1](https://github.com/jrappen/sublime-auto-dark/issues/1)

### Bug Fixes

* **Python:** Don't print error when light on macOS ([7c566bd](https://github.com/jrappen/sublime-auto-dark/commit/7c566bdda4460cd71d42730cd2ace4d929c7af0e))

# [1.2.0](https://github.com/jrappen/sublime-auto-dark/compare/1.1.0...1.2.0) (2020-03-12)

### Features

* **docs:** Ship changelog with package ([7f59f4b](https://github.com/jrappen/sublime-auto-dark/commit/7f59f4b517a187cb9fba2f015bcaf251a37e0402))

### Bug Fixes

* **GitHub:** Update issue template ([b118cb4](https://github.com/jrappen/sublime-auto-dark/commit/b118cb4dd91606afa2af6a0be05ab7cfab263b09))
* **PkgCtrl:** Update metadata labels ([18b668b](https://github.com/jrappen/sublime-auto-dark/commit/18b668b0a751b828d37464d4b63a14da06c25e54))
* **Python:** Unload plugin & better debug printing ([f8c7c3c](https://github.com/jrappen/sublime-auto-dark/commit/f8c7c3c74072f1890ef45d95da74b38dfab17dc5))
* **Python:** Fix logic of detecting dark mode ([cbe416d](https://github.com/jrappen/sublime-auto-dark/commit/cbe416d3eb26bb1fa4f1952ad035fa3539642583))
* **docs:** Fix wording of description ([79c2c5b](https://github.com/jrappen/sublime-auto-dark/commit/79c2c5b3263c39c8cfbd8581804468ecda19b154))
* **docs:** Update usage description ([88cca1c](https://github.com/jrappen/sublime-auto-dark/commit/88cca1cd8fdeb21d1bf59f721fe92a76eb35152d))
* [requested changes from `wbond/package_control_channel#7846`](https://github.com/wbond/package_control_channel/issues/7846#issuecomment-597317204):
    * **PkgCtrl:** Remove (implied) linux support ([73f58e8](https://github.com/jrappen/sublime-auto-dark/commit/73f58e8155f7495c74778e29f5c67894fd3ea5ec))
    * **Python:** Don't use a class ([e778640](https://github.com/jrappen/sublime-auto-dark/commit/e77864014a82785b4ee8d429fabeae2880f0ed3c))
* **PkgCtrl:** Slim down size of shipped package ([5d4c622](https://github.com/jrappen/sublime-auto-dark/commit/5d4c6224f91f1e4ae94684ff94d9932b763cec8c))
* **Python:** Fix typo ([c2b4d1f](https://github.com/jrappen/sublime-auto-dark/commit/c2b4d1fbbd85d9b44bed982991f3d26551ca7644))
* **Python:** Add more debugging code ([b6efbe8](https://github.com/jrappen/sublime-auto-dark/commit/b6efbe8db882fc6ce169866f7f702a4173e338cf))
* **Python:** Add missing arg `cls` ([27924dc](https://github.com/jrappen/sublime-auto-dark/commit/27924dcb790592ae75b5f1a52b142ca075e2388d))
* **Python:** Fix readability of Python source ([313fd13](https://github.com/jrappen/sublime-auto-dark/commit/313fd1370305993c0e4e7a71d0eeed73b7425198))

# [1.1.0](https://github.com/jrappen/sublime-auto-dark/compare/1.0.0...1.1.0) (2020-03-09)

### Features

* **Package Control:** Add PkgCtrl channel file ([db3a69e](https://github.com/jrappen/sublime-auto-dark/commit/db3a69ecdc3545c28f66f939b201b0bc3dfa9b67))

### Bug Fixes

* **Python:** Fix readability of Python source ([bab804e](https://github.com/jrappen/sublime-auto-dark/commit/bab804e5f1f87c9e89d3f4f83fd4b493064ca1a7))
* **Docs:** Use 4 spaces indentation for list items ([6d596bf](https://github.com/jrappen/sublime-auto-dark/commit/6d596bf3d96b47e5519b9522f2ee53ac9827e483))
* **Python:** Add missing `cls.` & use `with` ([1ad4d3c](https://github.com/jrappen/sublime-auto-dark/commit/1ad4d3c838bd2041a7a6c85a75b1d5d868a21206))
* **Python:** Remove unused parameter ([4bac492](https://github.com/jrappen/sublime-auto-dark/commit/4bac4929ab3e21fde0aca920a8cade938c271d12))
* **Python:** Fix painting on async & cleanup ([00e9ce8](https://github.com/jrappen/sublime-auto-dark/commit/00e9ce8e02a841d60bb0b5923cd46556d00c723c))
* **Python:** Fix code readability ([6d4378e](https://github.com/jrappen/sublime-auto-dark/commit/6d4378e3e3df52c9702e788ab44aa8f3db97d416))
* **Python:** Simplify dark mode detection ([1d0bc03](https://github.com/jrappen/sublime-auto-dark/commit/1d0bc039ecf0cb6501798044bcc40ebdd589528c))

# 1.0.0 (2020-03-04)

First release.
