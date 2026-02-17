# Backend Software Engineer - Take Home Test Assessment Rubric

This interview stage is for assessing a candidate's submission to the Take Home Test problem statement, and the barrier to entry is based on the question:

**"Is this submission worth a further conversation with the candidate?"**

Given the 90 min time allocation we recommend that candidates spend on completing the assignment, it's important to remember that we aren't looking for perfect solutions.

The result for each category should be one of:
- Pass
- Pass with concern
- Fail

Pass with concern is specifically there to highlight to the following interviewers your areas of concern, remember that the filter level for this interview stage is "is this worth a further conversation".

You may return a maximum of **one** "Pass with Concern" across all three areas, and still move to a Face to Face interview. If you have more than one rating of "Pass with Concern" across all three areas then raise it in the #interviews-dev-global channel before deciding whether or not to fail the candidate.

The submission should be failed if there are any areas that fall outside of the Pass or Pass with concern categories.

In all cases feedback should be recorded.

## 1. Programming Knowledge

| *Remember the time constraints on the candidate, you are looking for indicators not production ready code.* | |
| :---- | :---- |
| Pass | Code is readable. Code produces the required output. Appropriate encapsulation. Appropriate use of language features. Idiomatic code structure. |
| Pass With Concern | Writing an app. Unneeded dependencies. Poor type choice (e.g. float rather than decimal). GenAI is ok as long as they apply their knowledge on top. Unused or commented out code. Poor error handling. |

### Not required to pass
- Unless specifically required by the role (i.e. if we are looking to hire functional engineers), a functional approach is not required.

## 2. Testing

| *We expect TDD as a primary capability, not as a box ticking exercise. If there are no tests, that is a fail.* | |
| :---- | :---- |
| Pass | Reasonable code coverage. Test independence - tests can run in isolation from each other. HTTP client is tested. Adequate test assertions. No repeated tests - functionality is tested once. |
| Pass With Concern | Extraneous setup. Untestable components. Poor test naming. Unclear tests. Incomplete assertions. Dependency on "live" endpoint - Note that integration tests against a live endpoint are not considered as a warning. |

## 3. Design

| *The problem statement covers a small scope, the solution complexity should reflect this.* | |
| :---- | :---- |
| Pass | Minimal viable structure. Clear domain model. Appropriate dependencies. |
| Pass With Concern | Overly coupled components. Overly complicated. Large file count. |

### Not required to pass
- Updating the README with assumptions etc.
