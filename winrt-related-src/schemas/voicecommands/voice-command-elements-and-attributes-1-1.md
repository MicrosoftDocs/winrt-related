---
title: Voice Command Definition (VCD) elements and attributes v1.1
description: Reference documentation for the XML markup elements and attributes used in VCD files to specify recognition constraints.
Search.Product: eADQiWindows 10XVcnh
ms.assetid: af84a2cc-067e-456b-801a-1c3bc14f3bfe
keywords: windows 10, uwp, schema, cortana, voice commands, vcd
ms.topic: reference
ms.date: 04/05/2017
---

# Voice Command Definition (VCD) elements and attributes v1.1

> [!NOTE]
> The Cortana Skills Kit for consumer and enterprise, and the skills built on these platforms, have been deprecated.

See latest version at [**Voice Command Definition (VCD) elements and attributes v1.2**](voice-command-elements-and-attributes-1-2.md).

Reference documentation for the XML markup elements and attributes used in VCD files to specify recognition constraints.

Use voice commands to launch an app and specify an action or command to execute. For example, a user could tap the **Start** button and say "Contoso Widgets, show best sellers" to both launch the Contoso Widgets app and to navigate to a "best sellers" page.

## Elements and attributes

As with any XML file, a VCD file should begin with an XML declaration that specifies both the XML version and the character encoding.

```XML
<?xml version="1.0" encoding="utf-8"?>
```

The root element is the **VoiceCommands** element, and its **xmlns** attribute must be set to `http://schemas.microsoft.com/voicecommands/1.1` (no uppercase characters). For an example that conforms to this schema, see the [Cortana Voice Command sample](https://github.com/microsoft/Windows-universal-samples/blob/master/Samples/CortanaVoiceCommand/shared/AdventureWorksCommands.xml).

<table>
<tr>
<th colspan="2">Element</th><th>Description</th>
</tr>
<tr><td colspan="2">VoiceCommands</td>
<td>Required. The root element of a VCD file. Contains between 1 and 15 <strong>CommandSet</strong> elements, each of which represents the voice commands for a single language.</td>
</tr>
<tr>
<td colspan="2">CommandSet</td>
<td>Required child element of the <strong>VoiceCommands</strong> element. A container for all the voice commands that an app will accept in the language specified by the required <strong>xml:lang</strong> attribute. The value of the <strong>xml:lang</strong> attribute must be unique in the <strong>VoiceCommand</strong> document, and it is a single, specific language, specified in language name form, that corresponds to a language that is available in the <strong>Speech</strong> control panel. The <strong>Name</strong> attribute is optional and can be any arbitrary string; however, the <strong>Name</strong> attribute is required in order to reference and update a <strong>CommandSet</strong> element's <strong>PhraseList</strong> programmatically. The <strong>CommandSet</strong> element contains the following child elements: <strong>CommandPrefix</strong> (0 or 1), <strong>Example</strong> (exactly 1), <strong>Command</strong> (1 to 100), <strong>PhraseList</strong> elements (0 to 10), and <strong>PhraseTopic</strong> elements (0 to 10). These child elements must occur in the order listed.</td>
</tr>
<tr>
<td colspan="2">CommandPrefix</td>
<td>Optional child element of the <strong>CommandSet</strong> element. If present, must be the first child element of the <strong>CommandSet</strong> element. Specifies a user-friendly name for an app that a user can speak when giving a voice command. This is useful for apps with names that are long or are difficult to pronounce. Avoid using prefixes that conflict with other voice-enabled experiences.</td>
</tr>
<tr>
<td colspan="2">Command</td>
<td><p>Required child element of the <strong>CommandSet</strong> element.</p>
<p>Takes the <strong>Name</strong> attribute. Defines an app action that users can initiate by speaking and what users can say to initiate the action. Each <strong>Command</strong> element can be associated with a specific page in your app. Contains the following required child elements: <strong>Example</strong> (exactly 1), <strong>ListenFor</strong> (1 to 10), <strong>Feedback</strong> (exactly 1), and <strong>Navigate</strong> (exactly 1). These child elements must occur in the order listed.</p></td>
</tr>
<tr>
<td colspan="2">Example</td>
<td>Required child of both the <strong>CommandSet</strong> element and the <strong>Command</strong> element. Gives  a representative example of what a user can say for a <strong>CommandSet</strong> as a whole, and for an individual command. These examples will be will be visible to a user while viewing the <strong>What can I say</strong> screen on the phone. This screen appears when a user presses and holds the <strong>Search</strong> button and says, "Help" or "What can I say?", or taps <strong>See more</strong>. Examples should not include the name or prefix of the application, as this is handled automatically.</td>
</tr>
<tr>
<td colspan="2">ListenFor</td>
<td><p>Required (1 to 10) child element of the <strong>Command</strong> element. </p>
<p>Contains a word or phrase that your app will recognize for this command. This may include or be a reference to a <strong>PhraseList</strong> (or <strong>PhraseTopic</strong>) element's <strong>Label</strong> attribute, which appears in the <strong>ListenFor</strong> element enclosed in curly braces, for example: {myList}, or {myTopic}. </p>
<p>The content of any <strong>ListenFor</strong> elements can be recognized to activate the command. </p>
<p>Use brackets around a word or words that are optional. That is, the word or words can be spoken, but are not necessary for a match. For example, <code>&lt;ListenFor&gt;[Show] {options}&lt;/ListenFor&gt;</code>.</p>
<p>You can set up wildcard functionality by including an asterisk character inside a pair of curly braces, such as <code>&lt;ListenFor&gt; Find {*} &lt;/ListenFor&gt;</code>. In this example, the voice command will match as long as the user speaks "Find", optionally followed by any other word or phrase. If the voice command for a wildcard-enabled <strong>ListenFor</strong> element is matched, the  <a href="https://msdn.microsoft.com/library/windows/apps/windows.media.speechrecognition.speechrecognitionresult.text"><strong >SpeechRecognitionResult.Text</strong></a> property will contain the string "…" in the same position as the wildcard.</p></td>
</tr>
<tr>
<td colspan="2">Feedback</td>
<td>Required child element of the <strong>Command</strong> element. Specifies the text that will be displayed and read back to the user when the command is recognized. If the <strong>Feedback</strong> element includes a reference to a <strong>Label</strong> attribute of a <strong>PhraseList</strong> (or <strong>PhraseTopic</strong>) element, then every <strong>ListenFor</strong> element in the containing <strong>Command</strong> element must also reference the same <strong>Label</strong> attribute of the <strong>PhraseList</strong> (or <strong>PhraseTopic</strong>) element.</td>
</tr>
<tr>
<td colspan="2">
Navigate</td><td>Required child element of the <strong>Command</strong> element. The <strong>Target</strong> attribute is optional and is typically used to specify the page that the app should navigate to when it launches. You can obtain the value of the <strong>Target</strong> attribute (or the empty string if you omit the <strong>Target</strong> attribute) from the <a href="/uwp/api/Windows.Media.SpeechRecognition.SpeechRecognitionSemanticInterpretation"><strong>SpeechRecognitionSemanticInterpretation.Properties</strong></a> dictionary using the "NavigationTarget" key.</td>
</tr>
<tr>
<td colspan="2">PhraseList</td>
<td><p>Optional child of the <strong>CommandSet</strong> element. One <strong>CommandSet</strong> element can contain no more than 2,000 <strong>Item</strong> elements, and 2,000 <strong>Item</strong> elements is the combined total limit across all <strong>PhraseList</strong> elements in a <strong>CommandSet</strong>. Each <strong>Item</strong> specifies a word or phrase that can be recognized to initiate the command that references the <strong>PhraseList</strong>. The <strong>Items</strong> content may be programmatically updated from within your application. A <strong>PhraseList</strong> requires the <strong>Label</strong> attribute, the value of which may appear—enclosed by curly braces—inside <strong>ListenFor</strong> or <strong>Feedback</strong> elements, and is used to reference the <strong>PhraseList.</strong></p>
<p><strong>PhraseList</strong> has an optional <strong>Disambiguate</strong> attribute (default true), which specifies whether this <strong>PhraseList</strong> will produce user disambiguation when multiple items from the list are simultaneously recognized. When false, this <strong>PhraseList</strong> will also be unusable from within <strong>Feedback</strong> elements and will not produce parameters for your application. That's useful for phrases that are alternative ways of saying the same thing, but do not require any specific action.</p>
<p>In your app, to find out which phrase from the list was spoken, you can access the <a href="/uwp/api/Windows.Media.SpeechRecognition.SpeechRecognitionSemanticInterpretation"><strong>SpeechRecognitionSemanticInterpretation.Properties</strong></a> dictionary using a key with the same value as the <strong>Label</strong> of the <strong>PhraseList</strong>.</p>
</td>
</tr>
<tr>
<td colspan="2">Item</td>
<td>Optional child of the <strong>PhraseList</strong> element. One of multiple words or phrases that can be recognized to initiate a command. A <strong>CommandSet</strong> can contain no more than 2,000 <strong>Item</strong> elements across all of its child <strong>PhraseList</strong> elements.</td>
</tr>
<tr>
<td colspan="2">PhraseTopic</td>
<td><p>Optional child of the <strong>CommandSet</strong> element. Specifies a topic for large vocabulary recognition. The topic may specify a single (0 or 1) <strong>Scenario</strong> attribute  and several (0 to 20) <strong>Subject</strong> child elements for the scenario, which may be used to improve the relevance of the recognition achieved. A <strong>PhraseTopic</strong> requires the <strong>Label</strong> attribute, the value of which may appear—enclosed by curly braces—inside <strong>ListenFor</strong> or <strong>Feedback</strong> elements, and is used to reference the <strong>PhraseTopic</strong>.</p>
<p>The <strong>Scenario</strong> attribute (default "Dictation") specifies the desired scenario for this <strong>PhraseTopic</strong>, which may optimize the underlying speech recognition of voice commands using the <strong>PhraseTopic</strong> to produce results that are better-suited to the desired context of the command. Valid values are "Natural Language", "Search", "Short Message", "Dictation", "Commands", and "Form Filling".</p>
<p>The <strong>Subject</strong> child elements  specify a subject specific to the <strong>Scenario</strong> attribute of the parent <strong>PhraseTopic</strong> to further refine the relevance of speech recognition results within spoken commands using the <strong>PhraseTopic</strong>. Subjects will be evaluated in the order provided and, when appropriate, later-specified subjects will constrain earlier-specified ones. Valid inner text values are "Date/Time", "Addresses", "City/State", "Person Names", "Movies", "Music", and "Phone Number". For example: <code>&lt;Subject&gt;Phone Number&lt;/Subject&gt;</code> </p>
<p>In your app, to find out the content spoken in the subset of a <strong>ListenFor</strong> element represented by a <strong>PhraseTopic</strong> reference, you can access the <a href="/uwp/api/Windows.Media.SpeechRecognition.SpeechRecognitionSemanticInterpretation"><strong>SpeechRecognitionSemanticInterpretation.Properties</strong></a> dictionary using a key with the same value as the <strong>Label</strong> of the <strong>PhraseTopic</strong>.</p>
</td>
</tr>
</table>

> [!IMPORTANT]
> It’s not possible to nest the special characters listed below. For example, statements like ```[[start] new game]``` and ```[{myPhraseList}]``` are not possible.

<table>
<tr>
<th>Special character</th>
<th>Description</th>
</tr>
<tr>
<td>{}</td>
<td>Contains the value of the <strong>Label</strong> attribute for the <strong>PhraseList</strong> or <strong>PhraseTopic</strong> to reference, for example: {myList}, or {myTopic}. Used within a <strong>ListenFor</strong> or <strong>Feedback</strong> element. A <strong>PhraseList</strong> or <strong>PhraseTopic</strong> reference in a <strong>Feedback</strong> element must match a corresponding reference in a <strong>ListenFor</strong> element in the same command.</td></tr>
<tr><td>[]</td>
<td>Designates that the enclosed word or phrase is optional. The enclosed word or phrase may be spoken but is not required to be recognized to initiate the command. For example, if the contents of a <strong>ListenFor</strong> element are "[start] [begin] new game", the user can speak "start new game" or "new game" or "begin new game" (or even "start begin new game") to initiate the command. Each bracketed element is independently optional, but they must be spoken in the correct order to be recognized. So, in the "new game" example, "start begin new game" would work, but "begin start new game" would not work because of the order in which they were declared.</td></tr>
</table>


## See also

[Windows.ApplicationModel.VoiceCommands](/uwp/api/Windows.ApplicationModel.VoiceCommands)

[VCD elements and attributes v1.2](voice-command-elements-and-attributes-1-2.md)

[Cortana interactions](https://dev.microsoft.com/cortana)

**Designers**

[Cortana design guidelines](/cortana/voice-commands/voicecommand-design-guidelines)

**Samples**

[Cortana voice command sample](https://go.microsoft.com/fwlink/p/?LinkID=619899)
