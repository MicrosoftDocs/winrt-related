---
title: uap10:UpdateActions
description: Specifies what happens to files in the app's installation directory that are modified, added, or deleted by the app when it's updated to a new version.
ms.date: 07/07/2020
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap10:UpdateActions

For a desktop app in an MSIX package that uses the [uap10:InstalledLocationVirtualization](element-uap10-installedlocationvirtualization.md) extension, this element specifies what happens during app updates to files in the app's installation directory that were previously modified, added, or deleted by the app.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**[\uap10:Extension\>](element-uap10-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap10:InstalledLocationVirtualization\>](element-uap10-installedlocationvirtualization.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap10:UpdateActions\>**

## Syntax

```xml
<uap10:UpdateActions
    ModifiedItems = 'A string that can have one of the following values: "keep" or "reset".'
    DeletedItems = 'A string that can have one of the following values: "keep" or "reset".'
    AddedItems = 'A string that can have one of the following values: "keep" or "reset".' />
```

## Attrbutes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **ModifiedItems** | Specifies what happens during app updates to files in the app's installation directory that were previously modified by the app. This attribute only applies to files that were present in the app package when it was installed. | A string that can have one of the following values: "keep" or "reset". | Yes |  |
| **DeletedItems** | Specifies what happens during app updates to files in the app's installation directory that were previously deleted by the app. This attribute only applies to files that were present in the app package when it was installed. | A string that can have one of the following values: "keep" or "reset". | Yes |  |
| **AddedItems** | Specifies what happens during app updates to files in the app's installation directory that were added by the app after it was installed. | A string that can have one of the following values: "keep" or "reset". | Yes |  |

### Child elements

None

### Parent elements

| Parent element | Description |
|-|-|
| [uap10:InstalledLocationVirtualization](element-uap10-installedlocationvirtualization.md) | Defines an extension for a desktop app in an MSIX package that redirects any writes to the app's installation directory to a location in the [app data](/windows/uwp/design/app-settings/store-and-retrieve-app-data). For more details, see the [remarks](#remarks). |

### Remarks

This element can only be used in the context of the [uap10:InstalledLocationVirtualization](element-uap10-installedlocationvirtualization.md) extension. This extension redirects any writes to a desktop MSIX app's installation directory to a location in the [app data](/windows/uwp/design/app-settings/store-and-retrieve-app-data).

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
