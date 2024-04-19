---

title: uap10:InstalledLocationVirtualization
description: This extension redirects any writes to a desktop MSIX app's installation directory to a location in the app data.
ms.date: 07/07/2020
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap10:InstalledLocationVirtualization

Defines an extension for a desktop app in an MSIX package that redirects any writes to the app's installation directory to a location in the [app data](/windows/uwp/design/app-settings/store-and-retrieve-app-data). For more details, see the [remarks](#remarks).

## Element Hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap10:Extensions\>](element-uap10-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap10:InstalledLocationVirtualization\>**

## Syntax

```xml
<uap10:InstalledLocationVirtualization>

  <!-- Child elements -->
  uap10:UpdateActions

</uap10:InstalledLocationVirtualization>
```

## Attrbutes and elements

### Attributes

None.

### Child elements

| Child Element | Description |
|-|-|
| [uap10:UpdateActions](element-uap10-updateactions.md) | Specifies what happens during app updates to files in the app's installation directory that were previously modified, added, or deleted by the app. |

### Parent elements

| Parent element | Description |
|-|-|
| [uap10:Extension](element-uap10-extension.md) | Declares an extensibility point for the app. |

## Remarks

This extension is intended to be used by desktop apps in an MSIX package that write to their installation directory. These types of apps cannot normally write to their installation directory, so this extension redirects the write operations to a safe location in the [app data](/windows/uwp/design/app-settings/store-and-retrieve-app-data). This extension also enables you to specify what happens during app updates to files in the app's installation directory that were previously modified, added, or deleted by the app. This path redirection applies recursively to folders underneath the root folder. The extension has limited support for virtual file system (VFS) paths. 

This extension has no effect in a UWP app.

## Example

```xml
<?xml
  version="1.0"
  encoding="utf-8"
  standalone="yes"?>
<Package
  xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10"
  xmlns:uap10="http://schemas.microsoft.com/appx/manifest/uap/windows10/10"
  IgnorableNamespaces="uap10">

    <!-- Other entries omitted for brevity. -->

    <Extensions>
        <uap10:Extension
          Category="windows.installedLocationVirtualization">
            <uap10:InstalledLocationVirtualization>
            <uap10:UpdateActions
              ModifiedItems="keep"
              DeletedItems="reset"
              AddedItems="keep"/>
            </uap10:InstalledLocationVirtualization>
        </uap10:Extension>
    </Extensions>
</Package>
```

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
| **Minimum OS Version** | Windows 10 version 2004 (Build 19041) |
