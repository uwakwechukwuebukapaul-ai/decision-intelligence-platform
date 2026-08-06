"""
Dependency Graph

Builds and manages workflow
dependency relationships.

This module is intentionally
execution-agnostic. It simply
describes how workflow steps
relate to one another.
"""

from __future__ import annotations

from .execution_plan import ExecutionPlan
from .workflow import WorkflowStep


class DependencyGraph:
    """
    Represents the dependency graph
    for a workflow execution plan.
    """

    def __init__(
        self,
        execution_plan: ExecutionPlan,
    ):

        self.execution_plan = execution_plan

        self.steps: dict[str, WorkflowStep] = {}

        self.parents: dict[str, set[str]] = {}

        self.children: dict[str, set[str]] = {}

        self._build()

    def _build(
        self,
    ) -> None:
        """
        Construct dependency mappings.
        """

        for step in self.execution_plan.ordered_steps():

            self.steps[step.name] = step

            self.parents[step.name] = set(step.depends_on)

            self.children.setdefault(
                step.name,
                set(),
            )

        for step in self.execution_plan.ordered_steps():

            for dependency in step.depends_on:

                self.children.setdefault(
                    dependency,
                    set(),
                ).add(step.name)

    def root_steps(
        self,
    ) -> list[WorkflowStep]:
        """
        Steps without dependencies.
        """

        return [

            self.steps[name]

            for name, dependencies in self.parents.items()

            if not dependencies

        ]

    def child_steps(
        self,
        step_name: str,
    ) -> list[WorkflowStep]:
        """
        Children of a workflow step.
        """

        return [

            self.steps[name]

            for name in self.children.get(
                step_name,
                set(),
            )

        ]

    def parent_steps(
        self,
        step_name: str,
    ) -> list[WorkflowStep]:
        """
        Parent steps.
        """

        return [

            self.steps[name]

            for name in self.parents.get(
                step_name,
                set(),
            )

        ]

    def ready_steps(
        self,
        completed: set[str],
    ) -> list[WorkflowStep]:
        """
        Return every step whose
        dependencies have completed.
        """

        ready = []

        for name, dependencies in self.parents.items():

            if name in completed:

                continue

            if dependencies.issubset(completed):

                ready.append(
                    self.steps[name]
                )

        return ready

    def all_steps(
        self,
    ) -> list[WorkflowStep]:

        return list(
            self.steps.values()
        )

    def summary(
        self,
    ) -> dict:

        return {

            "steps": len(self.steps),

            "roots": len(
                self.root_steps()
            ),

            "edges": sum(
                len(children)
                for children in self.children.values()
            ),

        }