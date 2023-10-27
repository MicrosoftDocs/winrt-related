---
title: uap3:Verb
description: Defines the verbs associated with a file context menu (uap3:Verb).
ms.date: 11/26/2019
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap3:Verb

Defines the verbs associated with a file context menu and enables Windows Desktop Bridge apps to use ddeexec to launch.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:Extension\>](element-uap-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:FileTypeAssociation\>](element-uap-filetypeassociation.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap2:SupportedVerbs\>](element-uap2-supportedverbs.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap3:Verb\>**

## Syntax

```xml
<uap3:Verb
  Id = 'An alphanumeric string with a value between 3 and 64 characters in length.'
  Extended = 'An optional boolean value.'
  rescap3:DdeExecCommand = 'An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  rescap3:DdeExecApplication = 'An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  rescap3:DdeExecTopic = 'An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  rescap3:DdeExecIfExec = 'An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  uap7:Default = 'An optional boolean value.'
  Parameters = 'A string that contains one or more app parameters.'
  uap3:MultiSelectModel = 'A string that can be one of the following values: "Player", "Document", or "Single".' >
```

### Key

`?` optional (zero or one)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Id** | The name of the verb. | An alphanumeric string with a value between 3 and 64 characters in length. | Yes |  |
| **Extended** | Specifies that the verb should only appear if the user holds the *Shift* key before right-clicking the file to show the context menu. | An optional boolean value. | No |  |
| **rescap3:DdeExecCommand** | A DDE command string. | An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **rescap3:DdeExecApplication** | An application name used to establish the DDE conversion. | An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **rescap3:DdeExecTopic** | The topic name of the DDE conversion. | An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **rescap3:DdeExecIfExec** | The DDE command used if DDE conversion cannot be executed. | An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **uap7:Default** | Specifies whether the verb is the default verb. Only one verb within **SupportedVerbs** can be set as the default verb. | An optional boolean value. | No | False |
| **Parameters** | Specifies the parameters for the app. | A string that contains one or more app parameters. | No |  |
| **uap3:MultiSelectModel** | Specifies the activation model for apps that are started when the user selects and opens multiple files at the same time. For more information, see [this article](/windows/apps/desktop/modernize/desktop-to-uwp-extensions#define-how-your-application-behaves-when-users-select-and-open-multiple-files-at-the-same-time). | A string that can be one of the following values: *Player*, *Document*, or *Single*. | No |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [uap2:SupportedVerbs](element-uap2-supportedverbs.md) | Contains verbs for a file context menu. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/3` |
| Minimum OS Version | Windows 10 version 1607 (Build 14393) |
