---
title: com2:ProxyStubDll (in Package/Extensions)
description: Specifies the path and processor architecture of a ProxyStub DLL (in Package/Extensions).
ms.date: 10/10/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, com
---

# com2:ProxyStubDll (in Package/Extensions)

Specifies the path and processor architecture of a ProxyStub DLL.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extension\>](element-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<ComInterface\>](element-com-package-cominterface.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:Extension\>](element-com-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:ComInterface\>](element-com-cominterface.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:ProxyStub\>](element-com-package-proxystub.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com2:ProxyStubDll\>**

## Syntax

```xml
<com2:ProxyStubDll
  Path = 'A string with a value between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
  ProcessorArchitecture = 'A string that can have one of the following value: "x86", "x64", "arm", "arm64", or "x86a64".' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Path** | A relative path to the .dll file in the app package. | A string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | Yes |  |
| **ProcessorArchitecture** | The processor architecture of the ProxyStub registration. | A string that can have one of the following value: *x86*, *x64*, *arm*, *arm64*, or *x86a64*. | No |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [com:ProxyStub](element-com-package-proxystub.md) | Registers a proxy stub. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/2` |
| Minimum OS Version | Windows 10 version 1709 (Build 16299) |
