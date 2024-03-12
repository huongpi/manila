# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""add_backup_type_column

Revision ID: 2f27d904214c
Revises: 6e32091979e0
Create Date: 2024-03-10 23:16:18.130654

"""

# revision identifiers, used by Alembic.
revision = '2f27d904214c'
down_revision = '6e32091979e0'

from alembic import op
from oslo_log import log
import sqlalchemy as sa


LOG = log.getLogger(__name__)
share_backups_table_name = 'share_backups'
column_name = "backup_type"


def upgrade():
    try:
        op.add_column(share_backups_table_name,
                      sa.Column(column_name, sa.String(32), nullable=True))
    except Exception:
        LOG.error("Column 'backup_type' not created!")
        raise


def downgrade():
    try:
        op.drop_column(share_backups_table_name, column_name)
    except Exception:
        LOG.error("Column backup_type not dropped!")
        raise
