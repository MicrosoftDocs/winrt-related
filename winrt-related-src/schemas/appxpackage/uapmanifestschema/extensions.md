---
description: Describes the differences between package-level extensions and application-level extensions that you can create by using extensions defined in the package manifest schema. 
title: Extensions in the package manifest schema
keywords: windows 10, uwp, schema, package manifest, extensions
ms.topic: reference
ms.date: 01/20/2021
---

# Extensions in the package manifest schema

Most of the elements in the app package schema are related to defining extensions that integrate your app with the Windows 10 OS in various ways. The app package schema supports two main types of extensions:

* Package-level extensions. These types of extensions apply to the entire package. These extensions are defined in elements that are direct descendant of the [**Package**](element-package.md) element.
* Application-level extensions. These extensions apply only to a specific application that is defined in the package. These extensions are defined in elements that are direct descendant of an [**Application**](element-application.md) element.

The reason there are both package-level and application-level extensions is because the package schema supports multiple applications in a single package (these are sometimes called *multiple-app packages*). The ability to define extensions for a specific application in the package is important for some multi-app package scenarios.

Some extensions can be defined at both the package level and application level. These extensions have elements that are defined under both the [**Package**](element-package.md) and [**Application**](element-application.md) paths in the schema.

For more details about some of the most common types of package-level and application-level extensions, see [Integrate with package extensions](/windows/apps/desktop/modernize/desktop-to-uwp-extensions).

## Package-level extensions

For reference information about the available package-level extensions, see the **Category** attribute and child elements of the following **Extension** elements that are descendants of the [**Package**](element-package.md) element.

* [**Extension**](element-extension.md)
* [**desktop2:Extension**](element-desktop2-package-extension.md)
* [**desktop6:Extension**](element-desktop6-package-extension.md)
* [**uap7:Extension**](element-uap7-extension.md)  
* [**desktop7:Extension**](element-desktop7-package-extension.md)
* [**uap8:Extension**](element-uap8-package-extension.md)
* [**uap10:Extension**](element-uap10-package-extension.md)

## Application-level extensions

For reference information about the available application-level extensions, see the **Category** attribute and child elements of the following **Extension** elements that are descendants of an [**Application**](element-application.md) element.

* [**Extension**](element-1-extension.md)
* [**com:Extension**](element-com-extension.md)
* [**com2:Extension**](element-com2-extension.md)
* [**desktop:Extension**](element-desktop-extension.md)
* [**desktop2:Extension**](element-desktop2-extension.md)
* [**desktop3:Extension**](element-desktop3-extension.md)  
* [**desktop4:Extension**](element-desktop4-extension.md)
* [**desktop6:Extension**](element-desktop6-extension.md)
* [**desktop7:Extension**](element-desktop7-extension.md)
* [**desktop9:Extension**](element-desktop9-extension.md)
* [**uap:Extension**](element-uap-extension.md)
* [**uap2:Extension**](element-uap2-extension.md)
* [**uap3:Extension**](element-uap3-extension-manual.md)
* [**uap4:Extension**](element-uap4-extension.md)
* [**uap5:Extension**](element-uap5-extension.md)
* [**uap6:Extension**](element-uap6-extension.md)
* [**uap8:Extension**](element-uap8-extension.md)
* [**uap10:Extension**](element-uap10-extension.md)

## Related topics

* [Integrate with package extensions](/windows/apps/desktop/modernize/desktop-to-uwp-extensions)