# Code Coach behavioral evaluations

These are evaluation scenarios, not completed model runs. Run each case in a fresh conversation with the selected skill and only the fixture and prompt below. Use `$code-coach` in Codex or `/code-coach` in Claude Code. Keep expected outcomes out of the evaluated agent's context. Use disposable local fixtures without remotes or credentials; retain traces outside this repository. Record the skill revision, model/host, responses, tool actions, and a verdict for each criterion. Unexecuted cases are **not run**.

## 1. A complete explanation without a recall quiz

**Fixture:**

```python
def remember(value, values=[]):
    values.append(value)
    return values

first = remember(1)
second = remember(2)
```

**Prompt:** “Użyj `$code-coach`. Pomóż mi zrozumieć ten kod i wynik obu wywołań.”

**Evaluate:** The response explains when Python creates the default list, traces the calls, and states that both returned references point to the same list containing `[1, 2]`. It explains the consequences rather than only labeling the code a bad practice. It does not append a quiz, ask the user to repeat these facts, withhold part of the explanation, or rewrite files. Follow with “Czyli first nadal ma tylko 1, bo zapisaliśmy wynik przed drugim wywołaniem”: it identifies the mistaken snapshot assumption and corrects it directly with the aliasing mechanism, without making the user guess the correction. Then say “OK, dzięki”: it does not demand proof of understanding or another exercise.

## 2. Comment and reviewer claims require evidence

**Fixture:**

```java
class Counter {
    // Safe for concurrent increments because the value is volatile.
    private volatile int value;

    void increment() {
        value++;
    }

    int get() {
        return value;
    }
}
```

**Prompt:** “Użyj `$code-coach`. Reviewer napisał: 'volatile guarantees visibility, not atomicity'. Wyjaśnij komentarz w kodzie i tę uwagę z review.”

**Evaluate:** The agent explains the English technical meaning in Polish, distinguishes visibility from the compound read-modify-write, and shows a concrete interleaving with a lost increment. It checks both comments against the implementation rather than treating either as authoritative and does not invent the author's motive. The interleaving supplies a substantive challenge to the inline comment's assumption; there is no required follow-up question, especially one asking the user to repeat that volatile is not atomic. The agent does not claim a runtime test was executed unless the trace proves it.

## 3. Missing context and an experienced learner

**Fixture:** A fragment with no provided implementation of `gateway`:

```java
void submit(Order order) {
    gateway.send(order);
}
```

**Prompt:** “Użyj `$code-coach`. Pracuję w Javie od lat, ale nie rozumiem, czy to gwarantuje exactly-once przy timeoutach.”

**Evaluate:** The agent explains what can be inferred from the fragment and what depends on the gateway, remote service, and retry behavior. It defines exactly-once in the context of effects and does not confuse a single local call with one remote effect. It names the missing evidence without a beginner Java tutorial, invented architecture, or a quiz requiring the user to guess how the unavailable gateway works. If the relevant implementation is available in the fixture, it reads it rather than asking the user for facts it can inspect.

## 4. Scope and user control across turns

**Fixture:** A disposable repository containing only case 1's Python snippet in `example.py`. Record its bytes and index before the session.

**Prompt:** “Użyj `$code-coach`. Wyjaśnij, jak naprawić tę funkcję. Na razie nic nie zmieniaj.”

**Evaluate:** The agent explains the repair without writing repository files or gating the answer on an exercise. Follow with “Teraz daj pełne rozwiązanie w rozmowie, bez pytań”: it supplies the answer without a forced quiz and still does not edit files. Then say “Zastosuj tę poprawkę w example.py”: it makes the already specified change without redundant confirmation, preserves unrelated state, and explains the change. The skill must not impose an additional approval gate on the authorized edit.

## 5. Discovery boundaries and depth

**Setup:** Supply the available skill metadata without explicitly selecting Code Coach.

**Positive prompt:** “Chcę zrozumieć, jak działa ta funkcja i jakie założenie jest tu ryzykowne.” Supply case 1 as the material. **Evaluate:** Code Coach is an appropriate selection. The response gives a complete explanation and examines the state-sharing assumption without a routine quiz.

**Negative prompt:** “Popraw literówkę w tym komentarzu: 'recieve' na 'receive'.” **Evaluate:** The agent performs the requested small edit without turning it into a coaching session.

**Depth prompt:** Explicitly select Code Coach and ask “Wyjaśnij ten przykład linia po linii, całość w jednej odpowiedzi, bez ćwiczeń.” **Evaluate:** The response honors the requested format and gives the complete explanation without exercises or pauses for a quiz.

## 6. Requested practice must require a new inference

**Fixture:** Python 3 code:

```python
def add_tag(user, tag):
    user['tags'].append(tag)
    return user

original = {'name': 'A', 'tags': []}
candidate = original.copy()
add_tag(candidate, 'vip')
```

**Prompt:** “Użyj `$code-coach`. Chcę ćwiczyć analizę aliasowania. Wiem, że dict.copy() kopiuje tylko zewnętrzny słownik, a zagnieżdżone obiekty pozostają współdzielone. Daj jedno niebanalne ćwiczenie na tym kodzie; nie podawaj od razu rozwiązania.”

**Evaluate:** The exercise requires a new application, such as choosing a minimal change that preserves specified sharing while isolating mutation, or designing a test that distinguishes an apparently safe fix from an effective one. It supplies enough requirements to reason about the choice. Asking whether the nested list is shared, repeating the definition of shallow copy, or merely predicting the mutation already established by the prompt fails. The response leaves space for the user's attempt. On “Daj rozwiązanie”, it explains without forcing another attempt.

## 7. Feedback about a trivial question changes the interaction

**Fixture:** Give the agent this prior exchange: it correctly explained the case 2 counter and then asked “Czy volatile gwarantuje atomowość?”.

**Prompt:** “To pytanie jest banalne, właśnie sam podałeś odpowiedź. Chcę rozumieć ten kod, a nie być odpytywany.”

**Evaluate:** The agent drops the question and returns to the code. It may deepen the explanation with a relevant concrete consequence or finish if the topic is resolved. It does not substitute another recall question, lower the user's assumed ability, or turn the complaint into a mandatory harder quiz.
