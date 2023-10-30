---
description: Declares an app extensibility point of type windows.autoPlayContent (Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: uap:AutoPlayContent (Windows 10)
ms.assetid: 15514696-9195-4dd1-91af-2b97383992cc
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# uap:AutoPlayContent (Windows 10)

Declares an app extensibility point of type **windows.autoPlayContent**. The app provides the specified AutoPlay content actions.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:Extension\>](element-uap-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap:AutoPlayContent\>**

## Syntax

```xml
<uap:AutoPlayContent>

  <!-- Child elements -->
  uap:LaunchAction{1,1000}

</uap:AutoPlayContent>
```

### Key

`{}`  specific range of occurrences

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [uap:LaunchAction (in type: CT_AutoPlayContent)](element-uap-launchaction.md) | Describes an AutoPlay content action. |

### Parent elements

| Parent element | Description |
|-|-|
| [uap:Extension](element-uap-extension.md) | Declares an extensibility point for the app. |

## Remarks

When a volume-based device is connected to a computer or a disc is inserted into a CD or DVD drive, the system raises an AutoPlay content event. This extensibility point enables your app to be listed as an AutoPlay choice for one or more AutoPlay content events.

You can use any value for the **Verb** attribute except, **open**, which is reserved.

## Examples

```xml
<uap:Extension
  Category="windows.autoPlayContent">
  <uap:AutoPlayContent>
    <uap:LaunchAction
      Verb="show"
      ActionDisplayName="Show Pictures"
      ContentEvent="ShowPicturesOnArrival"/>
  </uap:AutoPlayContent>
</uap:Extension>
```

## See also

**Tasks**
[Auto-launching with AutoPlay](/previous-versions/windows/apps/hh452731(v=win.10))

**Concepts**
[App contracts and extensions](/previous-versions/windows/apps/hh464906(v=win.10))

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |
