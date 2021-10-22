---

title: desktop7:DesktopApp
description: Specifies the source and target for a tile or pin that should be updated as part of a desktop app migration.
ms.date: 10/15/2021
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop7:DesktopApp

## Description
Specifies the source and target for a tile or pin that should be updated as part of a desktop app migration.

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
<dt><a href="element-desktop7-extension.md">&lt;desktop7:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop7-shortcut.md">&lt;desktop7:Shortcut&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop7-desktopappmigration.md">&lt;desktop7:DesktopAppMigration&gt;</a></dt>
<dd><b>&lt;desktop7:DesktopApp&gt;</b></dd>
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
</dd>
</dl>


## Syntax

```xml
<desktop7:DesktopApp AumId   = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
                        ShortcutPath   = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. 
                        Executable   = A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", |, ?, or *. 
                         >
</desktop7:DesktopApp>
```


## Attributes and Elements

### Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| AumId | The Application User Model ID of the Desktop app to be migrated from. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |
| ShortcutPath | The relative shortcut path (.lnk) to migrate from. | Yes |
| Executable | The executable to which shortcuts should be migrated. | A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", \|, ?, or *. | Yes |

### Child Elements

None.

### Parent Elements

| Parent Element | Description |
|---------------|-------------|
| [DesktopAppMigrations](element-desktop7-desktopappmigration.md) | Specifies a set of app migration entries for tiles and pins. |  


## Remarks



## Requirements

|               |     Value                                                        |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/7` |