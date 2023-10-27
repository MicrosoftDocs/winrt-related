---
description: Defines an attribute of the class that is stored in the Windows Runtime property store (in Package/Applications).
title: uap5:ActivatableClassAttribute 
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 10/10/2017
---

# uap5:ActivatableClassAttribute 

Defines an attribute of the class that is stored in the Windows Runtime property store.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap5:Extension\>](element-uap5-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap5:OutOfProcessServer\>](element-uap5-outofprocessserver.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap5:ActivatableClass\>](element-uap5-activatableclass.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap5:ActivatableClassAttribute\>**

## Syntax

```xml
<ActivatableClassAttribute
  Name  = 'An alphanumeric string with a value between 1 and 255 characters in length. Must begin with a letter.'
  Type  = 'A string that can have one of the following values: "string" or "integer".'
  Value = 'A string with a value between 1 and 255 characters in length.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the attribute. | An alphanumeric string with a value between 1 and 255 characters in length. Must begin with a letter. | Yes |  |
| **Type** | The type of the attribute. | A string that can have one of the following values: *string* or *integer*. | Yes |  |
| **Value** | The value of the attribute. | A string with a value between 1 and 255 characters in length. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [uap5:ActivatableClass](element-uap5-activatableclass.md) | Declares a runtime class associated with the extensibility point. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/5` |
| Minimum OS Version | Windows 10 version 1709 (Build 16299) |
