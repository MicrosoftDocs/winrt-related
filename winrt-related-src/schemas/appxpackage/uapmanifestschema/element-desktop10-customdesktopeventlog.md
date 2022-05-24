---
title: desktop10:CustomDesktopEventLog
description: TBD
keywords: windows 10, uwp, schema, manifest, desktop, extension

ms.date: 05/23/2022
ms.topic: reference
---

# desktop10:CustomDesktopEventLog

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
<dd><strong>&lt;desktop10:CustomDesktopEventLog&gt;</strong></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

```xml
<desktop10:CustomDesktopEventLog
  CustomEvenLogName? = A string value between 1 and 32767 characters in length that cannot start or end with a whitespace character. May contain whitespace characters in between the first and last values.
  DisplayNameFile?   = A string between 1 and 256 characters in length that must end with ".dll" and cannot contain these characters: <, >, :, ", |, ?, or *.
  DisplayNameID?     = An unsigned integer value. A number between -2147483648 and 2147483647.
  MaxSize?           = An unsigned integer value. A number between -2147483648 and 2147483647.
  PrimaryModule?     = A string value between 1 and 32767 characters in length that cannot start or end with a whitespace character. May contain whitespace characters in between the first and last values.
  Retention?         = An unsigned integer value. A number between -2147483648 and 2147483647.
  >

</desktop10:CustomDesktopEventLog>
```

### Key

`?` optional (zero or one)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required |
|-|-|-|-|
| CustomEventLogName | TBD | A string value between 1 and 32767 characters in length that cannot start or end with a whitespace character. May contain whitespace characters in between the first and last values. | No |
| DisplayNameFile | TBD | A string between 1 and 256 characters in length that must end with ".dll" and cannot contain these characters: <, >, :, ", &#124;, ?, or *. | No |
| DisplayNameID | TBD | An unsigned integer value. A number between -2147483648 and 2147483647. | No |
| MaxSize | TBD | An unsigned integer value. A number between -2147483648 and 2147483647. | No |
| PrimaryModule | TBD | A string value between 1 and 32767 characters in length that cannot start or end with a whitespace character. May contain whitespace characters in between the first and last values. | No |
| Retention | TBD | An unsigned integer value. A number between -2147483648 and 2147483647. | No |

### Child Elements

| Child element | Description |
|-|-|
| [desktop10:CustomEventSource](element-desktop10-customeventsource.md) | TBD |

### Parent Elements

| Parent element | Description |
|-|-|
| [desktop10:Extension](element-desktop10-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Namespace | Value |
|-|-|
| **desktop10** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |