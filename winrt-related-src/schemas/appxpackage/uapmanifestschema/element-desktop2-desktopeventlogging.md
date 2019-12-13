---

ms.assetid: dbddff21-f1f6-488d-9ad5-12a3365a00e3
title: desktop2:DesktopEventLogging
description: Enables Windows Desktop Bridge apps to register for Windows event logging.

ms.date: 04/05/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop2:DesktopEventLogging

## Description
Enables Windows Desktop Bridge apps to register for Windows event logging.

## Element Hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop2-package-extension.md">&lt;desktop2:Extension&gt;</a></dt>
<dd><b>&lt;desktop2:DesktopEventLogging&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<desktop2:DesktopEventLogging AppName = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. >

  <!-- Child elements -->
  ( desktop2:EventMessageFiles,
    desktop2:TypesSupported )

</desktop2:DesktopEventLogging>
```

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| AppName | The name of the app that will use desktop event logging. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |

## Child Elements
| Child Element | Description |
|---------------|-------------|
| [EventMessageFiles](element-desktop2-eventmessagefiles.md) | Contains event message files. |
| [TypesSupported](element-desktop2-typessupported.md) | Contains the event log types that are supported. |

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/desktop/windows10/2</p></td>
</tr>
</tbody>
</table>