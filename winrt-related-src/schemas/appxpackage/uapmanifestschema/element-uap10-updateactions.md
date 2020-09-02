---
title: uap10:UpdateActions
description: Specifies what happens to files in the app's installation directory that are modified, added, or deleted by the app when it's updated to a new version.
ms.date: 07/07/2020
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap10:UpdateActions

## Description

For a desktop app in an MSIX package that uses the [uap10:InstalledLocationVirtualization](element-uap10-installedlocationvirtualization.md) extension, this element specifies what happens during app updates to files in the app's installation directory that were previously modified, added, or deleted by the app.

## Element Hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap10-extension.md">&lt;uap10:Extension&gt;</a></dt>
</dl>
<dl>
<dt><a href="element-uap10-installedlocationvirtualization.md">&lt;uap10:InstalledLocationVirtualization&gt;</a></dt>
<dd><b>&lt;uap10:UpdateActions&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

```syntax
<uap10:UpdateActions ModifiedItems = String value. Can be one of the following: "keep", "reset".
                     DeletedItems = String value. Can be one of the following: "keep", "reset".
                     AddedItems = String value. Can be one of the following: "keep", "reset". />
```

## Attrbutes and Elements

### Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| ModifiedItems | Specifies what happens during app updates to files in the app's installation directory that were previously modified by the app. This attribute only applies to files that were present in the app package when it was installed. | String. Can be one of the following: "keep", "reset" | Yes |
| DeletedItems | Specifies what happens during app updates to files in the app's installation directory that were previously deleted by the app. This attribute only applies to files that were present in the app package when it was installed. | String. Can be one of the following: "keep", "reset" | Yes |
| AddedItems | Specifies what happens during app updates to files in the app's installation directory that were added by the app after it was installed.  | String. Can be one of the following: "keep", "reset" | Yes |

### Child Elements

None

### Remarks

This element can only be used in the context of the [uap10:InstalledLocationVirtualization](element-uap10-installedlocationvirtualization.md) extension. This extension redirects any writes to a desktop MSIX app's installation directory to a location in the [app data](/windows/uwp/design/app-settings/store-and-retrieve-app-data).

## Example

```xml
<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<Package xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10"
         xmlns:uap10="http://schemas.microsoft.com/appx/manifest/uap/windows10/10"
         IgnorableNamespaces="uap10">

  <!-- Other entries omitted for brevity. -->

    <Extensions>
        <uap10:Extension Category="windows.installedLocationVirtualization">
            <uap10:InstalledLocationVirtualization>
            <uap10:UpdateActions ModifiedItems="keep" DeletedItems="reset" AddedItems="keep"/>
            </uap10:InstalledLocationVirtualization>
        </uap10:Extension>
    </Extensions>
</Package>
```

## Requirements

|   |   |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |