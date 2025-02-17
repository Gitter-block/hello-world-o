# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2021-2023 Valory AG
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""This module contains the shared state for the Hello World application."""

from typing import Any

from packages.valory.skills.abstract_round_abci.models import ApiSpecs, BaseParams
from packages.valory.skills.abstract_round_abci.models import (
    BenchmarkTool as BaseBenchmarkTool,
)
from packages.valory.skills.abstract_round_abci.models import Requests as BaseRequests
from packages.valory.skills.abstract_round_abci.models import (
    SharedState as BaseSharedState,
)
from packages.valory.skills.hello_world_abci.rounds import Event, HelloWorldAbciApp


MARGIN = 5


Requests = BaseRequests
BenchmarkTool = BaseBenchmarkTool


class SharedState(BaseSharedState):
    """Keep the current shared state of the skill."""

    abci_app_cls = HelloWorldAbciApp

    def setup(self) -> None:
        """Set up."""
        super().setup()
        HelloWorldAbciApp.event_to_timeout[
            Event.ROUND_TIMEOUT
        ] = self.context.params.round_timeout_seconds
        HelloWorldAbciApp.event_to_timeout[Event.RESET_TIMEOUT] = (
            self.context.params.reset_pause_duration + MARGIN
        )


class HelloWorldParams(BaseParams):
    """Hello World skill parameters."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the parameters."""
        self.hello_world_string: str = self._ensure("hello_world_message", kwargs, str)
        self.owner_ethereum_address: str = self._ensure("owner_ethereum_address", kwargs, str)#added
        super().__init__(*args, **kwargs)


RandomnessApi = ApiSpecs
