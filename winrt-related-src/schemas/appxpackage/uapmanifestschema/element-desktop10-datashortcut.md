---
title: desktop10:DataShortcut
description: TBD
keywords: windows 10, uwp, schema, manifest, desktop, extension

ms.date: 05/23/2022
ms.topic: reference
---

# desktop10:DataShortcut

## Description

TBD

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop10-extension.md">&lt;desktop10:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop10-datashortcuts.md">&lt;desktop10:DataShortcuts&gt;</a></dt>
<dd><strong>&lt;desktop10:DataShortcut&gt;</strong></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

```xml
<desktop10:DataShortcut
  Path              = A string between 1 and 256 characters in length that  cannot contain these characters: <, >, :, ", |, ?, or *.
  WorkingDirectory? = A string between 1 and 256 characters in length that  cannot contain these characters: <, >, :, ", |, ?, or *.
  WindowOption?     = A string value that can be one of the following: "minimized", "maximized", or "normal".
  Comment?          = A string value between 1 and 2048 characters.
  DisplayName       = An alphanumeric string value between 1 and 256 characters in length.
  Icon?             = A string between 1 and 256 characters in length that  cannot contain these characters: <, >, :, ", |;, ?, or *.
  IconIndex?        = A numerical value between 0 and 255.
  AUMID?            = A string value between 1 and 32767 characters that cannot begin or end with a whitespace character.
  >

</desktop10:DataShortcut>
```

### Key

`?` optional (zero or one)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required |
|-|-|-|-|
| Path | TBD | A string between 1 and 256 characters in length that  cannot contain these characters: <, >, :, ", &#124;, ?, or *. | Yes |
| WorkingDirectory | TBD | A string between 1 and 256 characters in length that  cannot contain these characters: <, >, :, ", &#124;, ?, or *. | No |
| WindowOption | TBD | A string value that can be one of the following: "minimized", "maximized", or "normal". | No |
| Comment | TBD | A string value between 1 and 2048 characters. | No |
| DisplayName | TBD | An alphanumeric string value between 1 and 256 characters in length. | Yes |
| Icon | TBD | A string between 1 and 256 characters in length that  cannot contain these characters: <, >, :, ", &#124;, ?, or *. | No |
| IconIndex | TBD | A numerical value between 0 and 255. | No |
| AUMID | TBD | A string value between 1 and 32767 characters that cannot begin or end with a whitespace character. | No | 

### Child Elements

None.

### Parent Elements

| Parent element | Description |
|-|-|
| [desktop10:DataShortcuts](element-desktop10-datashortcuts.md) | Declares an extensibility point for the app. |

## Requirements

| Namespace | Value |
|-|-|
| **desktop10** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |