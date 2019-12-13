---

ms.assetid: 1fe032ac-19b2-49a5-9f8f-093ab9102e66
title: uap4:MediaCodec
description: Defines an extension that enables an app to install media codecs from the Microsoft Store.

ms.date: 04/05/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap4:MediaCodec

## Description
Defines an extension that enables an app to install media codecs from the Microsoft Store.

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
<dt><a href="element-uap4-extension.md">&lt;uap4:Extension&gt;</a></dt>
<dd><b>&lt;uap4:MediaCodec&gt;</b></dd>
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
<uap4:MediaCodec DisplayName = A string between 1 and 256 characters in length. This string is localizable.
                 Description = A string between 1 and 2048 characters in length that cannot include characters such as tabs, carriage returns, and line feeds.
                 Category = One of the following string values: "audioDecoder", "audioEncoder","videoDecoder","videoEncoder"
                 AppServiceName? = A string between 2 and 39 characters in length that consists of alphanumeric, period (except for the first character), and dash characters only.
  <!-- Child elements -->
  uap4:MediaEncodingProperties
</uap4:MediaCodec>                   
```

### Key
`?` optional (zero or one)

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| DisplayName | The friendly name of the codec. | A string between 1 and 256 characters in length. This string is localizable. | Yes |
| Description | A description of the codec. | A string between 1 and 2048 characters in length that cannot include characters such as tabs, carriage returns, and line feeds. | Yes |
| Category | The category of the codec. | One of the following string values: <ul><li>audioDecoder</li><li>audioEncoder</li><li>videoDecoder</li><li>videoEncoder</li></ul> | Yes |
| AppServiceName | The app service that is launched as the codec. | A string between 2 and 39 characters in length that consists of alphanumeric, period (except for the first character), and dash characters only. | No |

## Child Elements 
| Child Element | Description |
|---------------|-------------|
| [MediaEncodingProperties](element-uap4-MediaEncodingProperties.md) | Contains the media coded input and output types. |

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/uap/windows10/4</p></td>
</tr>
</tbody>
</table>