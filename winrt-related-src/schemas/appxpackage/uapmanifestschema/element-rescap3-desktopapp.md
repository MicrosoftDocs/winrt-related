---

ms.assetid: d8525fc0-1289-4134-9d46-d294d39d2690
title: rescap3:DesktopApp
description: Specifies information for redirecting a Windows Desktop Bridge app's tiles and pins.

ms.date: 04/05/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# rescap3:DesktopApp


## Description
Specifies information for redirecting a Windows Desktop Bridge app's tiles and pins.

## Element Hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-rescap3-extension.md">&lt;rescap3:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-rescap3-desktopappmigration.md">&lt;rescap3:DesktopAppMigration&gt;</a></dt>
<dd><b>&lt;rescap3:DesktopApp&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<rescap3:DesktopApp AumId = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
                    ShortcutPath = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. >
```

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| AumId | The Application User Model ID of the Desktop app. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |
| ShortcutPath | A relative shortcut path to migrate from. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |

## Requirements

|               | Value                                                       |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities/3` |