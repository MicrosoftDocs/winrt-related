---

title: UAP3:Protocol
description: Declares an app extensibility point of type windows.protocol. A URI association indicates that the app is registered to handle URIs with the specified scheme.

ms.date: 03/14/2022
ms.topic: reference

keywords: windows 10, uwp, schema, manifest, extension 
---

# UAP3:Protocol

Declares an app extensibility point of type windows.protocol. A URI association indicates that the app is registered to handle URIs with the specified scheme.

[ <  Package  > ](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ < Applications > ](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ < Application > ](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ < UAP3:Extension > ](element-uap3-extension-manual.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**< UAP3:Protocol >**

## Syntax
```
<uap3:Protocol        parameters? = A string value or set of string values between % characters.
                      >

</uap3:Protocol>
```

### Key
`?` optional (zero or one)

### Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Parameters | The class ID associated with this media content. | A string value or set of string values between % characters. | No |

## Child Elements

None.

## Parent Elements

| Parent Element | Description |
|---------------|-------------|
| [uap3:Extension](element-uap3-extension-manual.md) | Sets parameters to define the protocol of the extensions. |


## Requirements
|   | Value |
|--|--|
| **uap3** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/3` |