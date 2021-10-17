import React from 'react';
import { CircularProgress, Divider, Grid, makeStyles, Theme } from '@material-ui/core';
import { AppBar } from './appBar';
import { getUrl } from '../appServices';
import { RequestFormType } from '../requestForm';
import { RequestForm } from './requestForm';
import { githubGist } from 'react-syntax-highlighter/dist/esm/styles/hljs'
import { encode } from "base-64";
import SyntaxHighlighter from 'react-syntax-highlighter';
import { ErrorContainer } from './errorContainer';

const useStyles = makeStyles((theme: Theme) => ({
    root: {
        height: "100vh",
        overflowY: "hidden",
        backgroundColor: theme.palette.grey[700],
    },
    requestForm: {
        height: "90vh",
        padding: "1px",
        backgroundColor: "#FFF",
    }

}));

interface MainProps { }

const Main = (props: React.PropsWithChildren<MainProps>) => {
    const [error, setError] = React.useState(null);
    const [loading, setLoading] = React.useState(false);
    const [result, setResult] = React.useState(null);

    const classes = useStyles();

    // const theme = {
    //     main: "line-height:1.3;background:#FFF;overflow:auto;",
    //     key: `color:${purple[700]}`,
    // };

    function handleErrors(response) {
        if (!response.ok) {
            throw Error(response.statusText);
        }
        return response.json();
    }

    const handleonClick = (requestForm: RequestFormType) => {
        setLoading(true);
        setResult(null);
        setError(null);

        fetch(getUrl(requestForm.id) + "?issentinel5p=" + requestForm.isSentinel5P.toString(), {
            method: 'GET',
            cache: "no-cache",
            headers: new Headers({
                'mode': 'cors',
                'Content-Type': 'application/json',
                'Authorization': 'Basic ' + encode(requestForm.username + ":" + requestForm.password),
            })
        })
            .then(handleErrors)
            .then(response => {
                setLoading(false);
                setResult(response["result"]);
                console.log(response);
            }).catch(error => {
                console.log("error " + error);
                setLoading(false);
                setError(error);
            });
    }

    return (
        <div>
            <Grid container className={classes.root} justify="center">
                <Grid item xs={12}>
                    <AppBar />
                </Grid>
                <Grid item container className={classes.requestForm} direction="row" justify="center" alignItems="center" xs={10}>
                    <Grid item style={{ width: "45%" }}>
                        <RequestForm
                            loading={loading}
                            submitRequest={handleonClick}
                        />
                    </Grid>
                    <Divider orientation="vertical" style={{ marginRight: "-1px" }} />
                    <Grid item container justify="center" alignItems="center" style={{ width: "55%", height: "inherit", overflow: "auto" }}>
                        {result &&
                            <Grid item style={{ width: "100%" }}>
                                <SyntaxHighlighter
                                    language='json'
                                    showLineNumbers={true}
                                    style={githubGist}
                                    wrapLongLines={true}
                                    wrapLines={true}
                                    lineProps={lineNumber => ({
                                        style: { display: 'block' },
                                        onClick() {
                                        }
                                    })}
                                >
                                    {JSON.stringify(result, null, 2)}
                                </SyntaxHighlighter>
                            </Grid>
                        }
                        {loading &&
                            <Grid item>
                                <CircularProgress size={60} color="secondary" />
                            </Grid>
                        }
                        {error && <ErrorContainer error={error.message} />}
                    </Grid>
                </Grid>
            </Grid>
        </div >
    );
}

export { Main }