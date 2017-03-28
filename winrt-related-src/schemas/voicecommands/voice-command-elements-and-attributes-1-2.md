---
title: Voice Command Definition (VCD) elements and attributes v1.2
description: Reference documentation for the XML markup elements and attributes used in Voice Command Definition (VCD) files to specify recognition constraints.
Search.Product: eADQiWindows 10XVcnh
ms.assetid: 697e3cef-ff82-4d9c-ab2f-d8ea4a4edfae
author: karl-bridge-microsoft
ms.author: kbridge
keywords: windows 10, uwp, schema, cortana, voice commands, vcd
ms.prod: windows
ms.technology: winrt-reference
ms.topic: reference
ms.date: 04/05/2017
---

# Voice Command Definition (VCD) elements and attributes v1.2


Reference documentation for the XML markup elements and attributes used in Voice Command Definition (VCD) files to specify recognition constraints.

Use voice commands to launch an app and specify an action or command to execute. For example, a user could tap the **Start** button and say "Contoso Widgets, show best sellers" to both launch the Contoso Widgets app and to navigate to a "best sellers" page.

## <span id="Elements_and_attributes"></span><span id="elements_and_attributes"></span><span id="ELEMENTS_AND_ATTRIBUTES"></span>Elements and attributes


As with any XML file, a VCD file should begin with an XML declaration that specifies both the XML version and the character encoding.

**Note**  Visual Studio includes this by default in new XML files.

 

```XML
<?xml version="1.0" encoding="utf-8"?>
```

Element
Description
VoiceCommands
Required. The root element of a VCD file. The value of its **xmlns** attribute must be **http://schemas.microsoft.com/voicecommands/1.2** (no uppercase characters). Contains between 1 and 15 **CommandSet** elements, each of which represents the voice commands for a single language.
CommandSet
Required child element of the **VoiceCommands** element. A container for all the voice commands that an app will accept in the language specified by the required **xml:lang** attribute.
The value of the **xml:lang** attribute must be unique in the **VoiceCommand** document, and it is a single, specific language, specified in language name form, that corresponds to a language that is available in the **Speech** control panel.

**Note**  Languages specified in the VCD file, but not supported on the system, are ignored.

The **Name** attribute is optional and can be any arbitrary string; however, the **Name** attribute is required in order to reference and update a **CommandSet** element's **PhraseList** programmatically. The **CommandSet** element contains the following child elements: **CommandPrefix** (0 or 1) or **AppName** (0 or 1), **Example** (exactly 1), **Command** (1 to 100), **PhraseList** elements (0 to 10), and **PhraseTopic** elements (0 to 10). These child elements must occur in the order listed.

Mutually exclusive
CommandPrefix
Optional child element of the **CommandSet** element. If present, must be the first child element of the **CommandSet** element.

Specifies a user-friendly name for an app that a user can speak when giving a voice command. This is useful for apps with names that are long or are difficult to pronounce.

Avoid using prefixes that conflict with other voice-enabled experiences.

AppName
Optional child element of the **CommandSet** element. If present, must be the first child element of the **CommandSet** element.

Replaces **CommandPrefix** and supports the **RequireAppName** attribute and `{builtin:AppName}` phrase of the **ListenFor** element.

Specifies a user-friendly name for an app that a user can speak when giving a voice command. This is useful for apps with names that are long or are difficult to pronounce.

Avoid using prefixes that conflict with other voice-enabled experiences.

By default, the **AppName** is supported as a suffix in the voice command.

Command
Required child element of the **CommandSet** element.

Takes the **Name** attribute. Defines an app action that users can initiate by speaking and what users can say to initiate the action. Each **Command** element can be associated with a specific page in your app. Contains the following required child elements: **Example** (exactly 1), **ListenFor** (1 to 10), **Feedback** (exactly 1), and **Navigate** (exactly 1). These child elements must occur in the order listed.

Example
Required child of both the **CommandSet** element (exactly 1) and the **Command** element (1 to 20). Gives a representative example of what a user can say for a **CommandSet** as a whole, and for an individual command. These examples will be visible to a user from the **What can I say** screen. This screen appears when a user presses and holds the **Search** button (on Windows phones) or invokes **Cortana** and says, "Help" or "What can I say?", or taps **See more**.
**Note**  Examples should include the **AppName** or **CommandPrefix**.

ListenFor
Required (1 to 20) child element of the **Command** element.

Contains a word or phrase that your app will recognize for this command. This may include or be a reference to a **PhraseList** (or **PhraseTopic**) element's **Label** attribute, which appears in the **ListenFor** element enclosed in curly braces, for example: {myList}, or {myTopic}.

The content of any **ListenFor** elements can be recognized to activate the command.

An optional **RequireAppName** attribute can be specified to indicate whether the value of the **AppName** element can be prepended, appended, or used inline with the **ListenFor** element.

This attribute supports four values:

-   **BeforePhrase**

    The user must say the **AppName** before the **ListenFor** phrase.

-   **AfterPhrase**

    The user must say "In|On|Using|With" **AppName** after the **ListenFor** phrase.

-   **BeforeOrAfterPhrase**

    The user must say the **AppName** before or after the **ListenFor** phrase.

-   **ExplicitlySpecified**

    The **AppName** is explicitly referenced in the **ListenFor**, using `{builtin:AppName}`. The user is not required to say the **AppName** before or after the **ListenFor** phrase.

Use brackets around a word or words that are optional. That is, the word or words can be spoken, but are not necessary for a match. For example, `<ListenFor>[Show] {options}</ListenFor>`.

You can set up wildcard functionality by including an asterisk character inside a pair of curly braces, such as `<ListenFor> Find {*} </ListenFor>`. In this example, the voice command will match as long as the user speaks "Find", optionally followed by any other word or phrase. If the voice command for a wildcard-enabled **ListenFor** element is matched, the [**SpeechRecognitionResult.Text**](https://msdn.microsoft.com/library/windows/apps/dn631441) property will contain the string "…" in the same position as the wildcard.

Feedback
Required child element of the **Command** element. Specifies the text that will be displayed and read back to the user when the command is recognized. If the **Feedback** element includes a reference to a **Label** attribute of a **PhraseList** (or **PhraseTopic**) element, then every **ListenFor** element in the containing **Command** element must also reference the same **Label** attribute of the **PhraseList** (or **PhraseTopic**) element.
Mutually exclusive
Navigate
Required child element of the **Command** element, unless the **Command** element has a **VoiceCommandService** child element. The **Target** attribute is optional and is typically used to specify the page that the app should navigate to when it launches. You can obtain the value of the **Target** attribute (or the empty string if you omit the **Target** attribute) from the [**SpeechRecognitionSemanticInterpretation.Properties**](https://msdn.microsoft.com/library/windows/apps/dn631445) dictionary using the "NavigationTarget" key.
VoiceCommandService
Required child element of the **Command** element, unless the **Command** element has a **Navigate** child element. This element specifies that the voice command is handled through an app service (see [**Windows.ApplicationModel.AppService**](https://msdn.microsoft.com/library/windows/apps/dn921731)) with feedback displayed on the **Cortana** canvas. The **Target** attribute is mandatory and must match the value of the **Name** attribute of the **AppService** element in the [app package manifest](https://msdn.microsoft.com/library/windows/apps/br211474).
PhraseList
Optional child of the **CommandSet** element. One **CommandSet** element can contain no more than 2,000 **Item** elements, and 2,000 **Item** elements is the combined total limit across all **PhraseList** elements in a **CommandSet**. Each **Item** specifies a word or phrase that can be recognized to initiate the command that references the **PhraseList**. The **Items** content may be programmatically updated from within your application. A **PhraseList** requires the **Label** attribute, the value of which may appear—enclosed by curly braces—inside **ListenFor** or **Feedback** elements, and is used to reference the **PhraseList.**

**PhraseList** has an optional **Disambiguate** attribute (default true), which specifies whether this **PhraseList** will produce user disambiguation when multiple items from the list are simultaneously recognized. When false, this **PhraseList** will also be unusable from within **Feedback** elements and will not produce parameters for your application. That's useful for phrases that are alternative ways of saying the same thing, but do not require any specific action.

In your app, to find out which phrase from the list was spoken, you can access the [**SpeechRecognitionSemanticInterpretation.Properties**](https://msdn.microsoft.com/library/windows/apps/dn631445) dictionary using a key with the same value as the **Label** of the **PhraseList**.

Item
Optional child of the **PhraseList** element. One of multiple words or phrases that can be recognized to initiate a command. A **CommandSet** can contain no more than 2,000 **Item** elements across all of its child **PhraseList** elements.
PhraseTopic
Optional child of the **CommandSet** element. Specifies a topic for large vocabulary recognition. The topic may specify a single (0 or 1) **Scenario** attribute and several (0 to 20) **Subject** child elements for the scenario, which may be used to improve the relevance of the recognition achieved. A **PhraseTopic** requires the **Label** attribute, the value of which may appear—enclosed by curly braces—inside **ListenFor** or **Feedback** elements, and is used to reference the **PhraseTopic**.

The **Scenario** attribute (default "Dictation") specifies the desired scenario for this **PhraseTopic**, which may optimize the underlying speech recognition of voice commands using the **PhraseTopic** to produce results that are better-suited to the desired context of the command. Valid values are "Natural Language", "Search", "Short Message", "Dictation", "Commands", and "Form Filling".

The **Subject** child elements specify a subject specific to the **Scenario** attribute of the parent **PhraseTopic** to further refine the relevance of speech recognition results within spoken commands using the **PhraseTopic**. Subjects will be evaluated in the order provided and, when appropriate, later-specified subjects will constrain earlier-specified ones. Valid inner text values are "Date/Time", "Addresses", "City/State", "Person Names", "Movies", "Music", and "Phone Number". For example: `<Subject>Phone Number</Subject>`

In your app, to find out the content spoken in the subset of a **ListenFor** element represented by a **PhraseTopic** reference, you can access the [**SpeechRecognitionSemanticInterpretation.Properties**](https://msdn.microsoft.com/library/windows/apps/dn631445) dictionary using a key with the same value as the **Label** of the **PhraseTopic**.

 

**Important Note:  **It’s not possible to nest the special characters listed below. For example, statements like `[[start] new game]` and `[{myPhraseList}]` are not possible.

| Special character | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| {}                | Contains the value of the **Label** attribute for the **PhraseList** or **PhraseTopic** to reference, for example: {myList}, or {myTopic}. Used within a **ListenFor** or **Feedback** element. A **PhraseList** or **PhraseTopic** reference in a **Feedback** element must match a corresponding reference in a **ListenFor** element in the same command.                                                                                                                                                                                                                                                                                                                |
| \[\]              | Designates that the enclosed word or phrase is optional. The enclosed word or phrase may be spoken but is not required to be recognized to initiate the command. For example, if the contents of a **ListenFor** element are "\[start\] \[begin\] new game", the user can speak "start new game" or "new game" or "begin new game" (or even "start begin new game") to initiate the command. Each bracketed element is independently optional, but they must be spoken in the correct order to be recognized. So, in the "new game" example, "start begin new game" would work, but "begin start new game" would not work because of the order in which they were declared. |

 

## <span id="see_also"></span>See also


[**Windows.ApplicationModel.VoiceCommands**](windows-applicationmodel-voicecommands.md)

[Cortana interactions](https://msdn.microsoft.com/library/windows/apps/mt185598)

**Designers**
[Cortana design guidelines](https://msdn.microsoft.com/library/windows/apps/dn974233)

**Samples**
[Cortana voice command sample](http://go.microsoft.com/fwlink/p/?LinkID=619899)

 

 




