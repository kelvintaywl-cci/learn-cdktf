#!/usr/bin/env python
import os

from cdktf import App, TerraformStack
from cdktf_cdktf_provider_pagerduty.provider import PagerdutyProvider
from cdktf_cdktf_provider_pagerduty.team import Team
from cdktf_cdktf_provider_pagerduty.team_membership import TeamMembership
from cdktf_cdktf_provider_pagerduty.user import User
from constructs import Construct


class PagerDuty(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)
        # FIXME: can we no supply the token args,
        # and let the Provider look up this $PAGERDUTY_TOKEN env var by default?
        PagerdutyProvider(self, "pagerduty", token=os.environ["PAGERDUTY_TOKEN"])

        team = Team(
            self,
            id_="it",
            name="Hello IT",
            description="Have you tried turning it off and on again?",
        )
        self.team = team
        self.users = []
        self.memberships = []

        for (id, name, email_prefix, title) in [
            (
                "maurice_moss",
                "Maurice Moss",
                "mmoss",
                "IT technician",
            ),
            (
                "roy_trenneman",
                "Roy Trenneman",
                "rtrenneman",
                "IT technician",
            ),
            ("jen_barber", "Jen Barber", "jbarber", "IT manager"),
        ]:
            email = f"{email_prefix}@reynholm.industries"
            user = User(self, id_=id, name=name, email=email, job_title=title)
            self.users.append(user)

            m = TeamMembership(
                self,
                id_=f"{email_prefix}_it",
                team_id=team.id,
                user_id=user.id,
            )
            self.memberships.append(m)


app = App()
PagerDuty(app, "learn-cdktf")

app.synth()
